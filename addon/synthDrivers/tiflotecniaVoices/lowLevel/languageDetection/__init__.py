# -*- coding: utf-8 -*-

from collections import defaultdict
from io import StringIO
from speech.commands import LangChangeCommand
from .blocks import BLOCKS, BLOCK_RSHIFT

BASIC_LATIN = [
    u"en", u"ha", u"so", u"id", u"la", u"sw", u"eu",
    u"nr", u"zu", u"xh", u"ss", u"st", u"tn", u"ts"
]
EXTENDED_LATIN = [
    u"cs", u"af", u"pl", u"hr", u"ro", u"sk", u"sl", u"tr", u"hu", u"az",
    u"et", u"sq", u"ca", u"es", u"gl", u"fr", u"de", u"nl", u"it", u"da", u"is", u"nb", u"sv",
    u"fi", u"lv", u"pt", u"ve", u"lt", u"tl", u"cy", u"vi", "no"
]
ALL_LATIN = BASIC_LATIN + EXTENDED_LATIN

CYRILLIC = [u"ru", u"uk", u"kk", u"uz", u"mn", u"sr", u"mk", u"bg", u"ky"]
ARABIC = [u"ar", u"fa", u"ps", u"ur"]
CJK = [u"zh", u"ja", u"ko"]

SINGLETONS = {
    u"Armenian" : u"hy",
    u"Hebrew" : u"he",
    u"Bengali" : u"bn",
    u"Gurmukhi": u"pa",
    u"Greek" : u"el",
    u"Gujarati" : u"gu",
    u"Oriya" : u"or",
    u"Tamil" : u"ta",
    u"Telugu" : u"te",
    u"Kannada" : u"kn",
    u"Malayalam" : u"ml",
    u"Sinhala" : u"si",
    u"Thai" : u"th",
    u"Lao" : u"lo",
    u"Tibetan" : u"bo",
    u"Burmese" : u"my",
    u"Georgian" : u"ka",
    u"Mongolian" : u"mn-Mong",
    u"Khmer" : u"km",
}

class LanguageDetector(object):
	def __init__(self, availableLanguages):
		availableLanguages = frozenset(l.split("_")[0] for l in availableLanguages)
		languageBlocks = defaultdict(lambda : [])
		for l in (set(ALL_LATIN) & availableLanguages):
			languageBlocks[l].extend([u"Basic Latin", u"Extended Latin"])
		for l in (set(CYRILLIC) & availableLanguages):
			languageBlocks[l].append(u"Cyrillic")
		for l in (set(ARABIC) & availableLanguages):
			languageBlocks[l].extend([u"Arabic", u"Arabic Presentation Forms-A", u"Arabic Presentation Forms-B"])
		if u"ko" in availableLanguages:
			for block in [u"Hangul Syllables", u"Hangul Jamo", u"Hangul Compatibility Jamo", u"Hangul"]:
				languageBlocks[u"ko"].append(block)
		if u"el" in availableLanguages:
			languageBlocks[u"el"].append(u"Greek and Coptic")
		if u"ja" in availableLanguages:
			languageBlocks[u"ja"].extend([u"Kana", u"CJK Unified Ideographs"])
		if u"zh" in availableLanguages:
			languageBlocks[u"zh"].extend([u"CJK Unified Ideographs", u"Bopomofo", u"Bopomofo Extended", u"KangXi Radicals"])
		for k, v in SINGLETONS.items():
			if v in availableLanguages:
				languageBlocks[v].append(k)
		self.languageBlocks = languageBlocks

		blockLanguages = defaultdict(lambda : [])
		for k, v in languageBlocks.items():
			for i in v:
				blockLanguages[i].append(k)
		self.blockLanguages = blockLanguages

	def add_detected_language_commands(self, speechSequence, defaultLang):
		sb = StringIO()
		charset = None
		curLang = defaultLang
		tmpLang = curLang.split("_")[0]
		for command in speechSequence:
			if isinstance(command, LangChangeCommand):
				if command.lang is None:
					curLang = defaultLang
				else:
					curLang = command.lang
				tmpLang = curLang.split("_")[0]
				yield command
				charset = None
			elif isinstance(command, str):
				sb = StringIO()
				command = str(command)
				prevInIgnore = False
				for c in command:
					block = ord(c) >> BLOCK_RSHIFT
					if c.isspace():
						sb.write(c)
						continue
					if c.isdigit() or (not c.isalpha() and block <= 0x8):
						if c.isdigit():
							sb.write(c)
							continue
						if not c.isdigit():
							sb.write(c)
							continue
						if prevInIgnore:
							sb.write(c)
							continue
						prevInIgnore = True
						charset = None
						if tmpLang != curLang.split("_")[0]:
							if sb.getvalue():
								yield sb.getvalue()
								sb = StringIO()
							yield LangChangeCommand(curLang)
							tmpLang = curLang.split("_")[0]
						sb.write(c)
						continue

					prevInIgnore = False
					newCharset = BLOCKS[block]
					if newCharset == charset:
						sb.write(c)
						continue
					charset = newCharset
					if charset in self.languageBlocks[tmpLang]:
						sb.write(c)
						continue
					newLang = self.find_language_for_charset(charset, curLang)
					newLangFirst = newLang.split("_")[0]
					if newLangFirst == tmpLang:
						sb.write(c)
						continue
					if sb.getvalue():
						yield sb.getvalue()
						sb = StringIO()
					tmpLang = newLangFirst
					if newLang == curLang:
						yield LangChangeCommand(newLang)
					else:
						yield LangChangeCommand(tmpLang)
					sb.write(c)
				if sb.getvalue():
					yield sb.getvalue()
			else:
				yield command

	def find_language_for_charset(self, charset, curLang):
		langs = self.blockLanguages[charset]
		if not langs or curLang.split("_")[0] in langs:
			return curLang
		return langs[0]
