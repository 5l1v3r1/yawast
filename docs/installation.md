---
layout: default
title: Installation
permalink: /installation/
---

### Installing

The simplest method on most platforms is to install is to use the Pip installer (for Windows, see below):

`pip3 install yawast`

This allows for simple updates (`pip3 install -U yawast`) and makes it easy to ensure that you are always using the latest version.

YAWAST requires Python 3.7, and is tested on Mac OSX, Linux, and Windows.

*Note:* There are additional dependencies required for certain scanning features starting with YAWAST 0.7.0; see the "Enhanced Vulnerability Scanner" section below for details.

#### Docker

YAWAST can be run inside a docker container.

```
docker pull adamcaudill/yawast && docker run --rm -it adamcaudill/yawast scan <url> ...
```

If you would like to capture the JSON output via the `--output=` option, you will need to use a slightly different command. The following example is for macOS, Linux, etc., for Windows, you will need to modify the command. The following mounts the current directory to the Docker image, so that it can write the JSON file: 

```
$ docker pull adamcaudill/yawast && docker run -v `pwd`/:/data/output/ --rm -it adamcaudill/yawast scan <url> --output=./output/
```

#### Kali Rolling

To install on Kali, just run:

```
pip3 install -U nassl
pip3 install yawast
```

#### Ubuntu

To install YAWAST, you first need to install a couple packages via `apt-get`:

```
sudo apt-get install python3.7
sudo pip3 install yawast
```

#### macOS

The version of Python shipped with macOS is too old, so the recommended solution is to use brew to install a current version:

```
brew install python
pip3 install yawast
```

#### Windows

There are two ways to use YAWAST on Windows, the easiest is to use the compiled EXE available on the [releases](https://github.com/adamcaudill/yawast/releases) page. This allows you to avoid installing Python and dealing with dependencies.

The other option is to install Python and use Pip; this option is somewhat complex on Windows due to the fact that some of the dependencies will need to be compiled. Due to these complexities, we generally recommend using the compiled version.

### Enhanced Vulnerability Scanner

Starting in YAWAST version 0.7.0, there is a new vulnerability scanner that performs tests that aren't possible using Python alone. To accomplish this, the new vulnerability scanner uses Chrome via Selenium, which adds a few additional dependencies:

* Google Chrome
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)

#### macOS

ChromeDriver can be installed via `brew` using the following commands:

```
brew tap homebrew/cask
brew cask install chromedriver
```

#### Linux

ChromeDriver for Linux can be install using the following commands; please make sure that you are using the latest stable release from the [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) web site.

```
wget https://chromedriver.storage.googleapis.com/73.0.3683.68/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

#### Windows

You can easily install ChromeDriver on Windows via a package manager such as [Chocolatey](https://chocolatey.org/docs/installation) using the following command:

```
choco install chromedriver
```