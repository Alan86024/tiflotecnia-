# Tiflotechnia Voices for NVDA Documentation

## Welcome

Thank you for choosing Tiflotechnia for your text to speech needs. You are about to experience the best in high-quality multilingual, responsive and natural speech synthesis. This documentation will familiarize you with all of the features this addon has to offer.

## System Requirements

This addon will run on the following configurations:
* Windows 10 or above
* Sufficient ram and disk space for all of the voices you wish to install. The amount of actual space depends on the voices in question, but here are a few general points of consideration:
    * Low quality variants are only ever a few megabytes in size, and thus take up the least ram.
    * The higher the quality, the greater the space and ram requirements. While the actual size differs depending on which voice is being used, a single voice at the highest quality generally never exceeds 300MB.
* NVDA 2023.1.0 or above is required to run the addon.

## Installation and Licensing

### Installing the Addon

To install the addon, simply click on the addon file and allow NVDA to install it. The addon will present itself once NVDA restarts.

### Licensing

The first time the addon launches, it will ask you to enter your license key. If you do not have one, you may select the "I want to try the product for 7 days" radio button by pressing down arrow until it is spoken. At this point, pressing tab will lead to the "Try the product for 7 days " button, which will generate a trial license upon activation. This license will allow you to access all of the features of the addon for 7 days from the date of activation.

#### Activating over the internet

Activating over the internet is the fastest way to license the product, and is recommended for most users. In order to activate over the internet:
1. When the registration screen appears, press enter.
1. Paste in the license key you received upon purchase, and then press enter.
1. If the license key is valid, you will be informed that activation has been successful.

#### Activating without an Internet Connection

If you are on a machine with a firewall or otherwise lack regular access to a working internet connection, you will be able to activate the product via an offline method. In order to activate without an internet connection, follow the below procedure:
1. When the registration screen appears, down arrow to the "Offline activation (for places without an internet connection)" radio button, then press enter.
1. Paste in the license key you received upon purchase, then press enter.
1. You will be presented with a file save dialog which will save a machine identification file. Select the directory in which you would like the file to be saved, then save the file.
1. Go to the [offline activation portal](https://activate.accessmind.net) in order to generate an offline activation key file. You will do this by uploading the machine identification file you received from the addon.
1. Once your key file has been downloaded, go back into the Offline Activation screen and activate the "Activate license" button.
1. Locate and select your license key file. If the key file is valid, you will be informed that product activation was successful.

### Installing Voices

Before you can use the synthesizer, you will need to install at least one voice. Voices can be installed via a built-in downloader. You will be asked if you would like to run the downloader upon initial license activation if no voices are present. You can also access this downloader from the newly created  "Tiflotecnia voices for NVDA" submenu in the NVDA menu (*Insert or Capslock+N*). Once in this menu, locate and activate the "Manage voices..." menu option.

Once inside the voice manager, you will first be presented with a language dropdown. Select the language you wish to install voices for by either using the up and down arrows to cycle through the list, or by pressing the first letter of the language you are looking for. Pressing tab from here will reveal the Quality dropdown. From here, you can select a voice quality you would like to get a listing of voices for. By default, all qualities are exposed. The available qualities are as follows:
* Lowest: small footprint, good for installations with lower ram.
    * Those coming from previous Vocalizer distributions may know these as compact variants
* Intermediate: Middle of the road option that balances decent quality with a relatively small memory footprint
    * Those coming from previous Vocalizer distributions may know these as standard (Automotive) or plus (Expressive) variants
* Enhanced: For most voices, this option presents the highest quality, but also carries the largest memory footprint.
    * Those coming from previous Vocalizer distributions may know these as premium or premium high variants
* Highest: This option is available for some of the voices, presenting an even higher ality than the enhanced option

If you do not wish to filter the voice quality, you can simply tab past this control. In any case, you will be presented with a list of voices. These list items are checkboxes, allowing you to select multiple at a time. Once you have selected the voices you wish to install, tab to the Install button and activate it. The button will report the number of voices you have enqueued for install. Once you activate the button, the downloads will begin. Each voice will be installed one at a time, but there is no further user interaction required. Thus, it is safe to let the installer run unattended at this point. Once the voice installation completes, you may select the new "Tiflotecnia voices for NVDA" option in your synthesizer dialogue.

#### Note

While it is possible to download voices while the synthesizer is running, the speech will cut out for a brief moment following the installation of each voice. This can make continuous reading slightly difficult if you are installing multiple voices at a time. Thus, we recommend switching your synthesizer during a batch installation. The downloader will continue to notify you about the status of the installations.

## Automatic Language Switching for Arabic text

If you have at least one Arabic, Hebrew or Cyrilic voice installed, you will be able to leverage our unique automatic language switching ability for switching between Latin and non-Latin texts. The new "Tiflotecnia voices for NVDA" setting group in the NVDA Settings dialog will allow you to select a voice to be used for Latin texts, as well as a voice to be used for non-Latin texts. In turn, the new "Automatically switch language based on unicode characters" option in the NVDA Voice Settings for the synthesizer will allow you to toggle this option.