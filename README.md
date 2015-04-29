gyp-getting-started
===================

For more information, see  

* [http://enginetrouble.net/2013/07/getting-started-with-gyp.html](http://enginetrouble.net/2013/07/getting-started-with-gyp.html)  
* [http://enginetrouble.net/](http://enginetrouble.net/)  

## Getting the code

```bash
git clone git://github.com/enginetrouble/gyp-getting-started.git
```

## Requirements

* Python 2.7+
* Xcode 5
* Visual Studio 2013

## How to build

### Prerequisite: Installing GYP

First, install GYP from https://chromium.googlesource.com/external/.  
Make sure `git` is installed.
From the root of your engine directory, run:

```bash
git clone https://chromium.googlesource.com/external/gyp.git tools/gyp
```

Second, run `setup.py`:

**Linux and Mac OSX**

To install globally with gyp:

```bash
cd tools/gyp
[sudo] python setup.py install
```

**Windows**

```bash
cd tools/gyp
python setup.py install
```

### Building under Xcode (Apple LLVM Clang++)

#### 1. Generate project

```bash
gyp build/trivial.gyp --depth=. -f xcode --generator-output=./build.xcodefiles/
```

#### 2. Build (Debug/Release)

```bash
xcodebuild -project build.xcodefiles/build/trivial.xcodeproj
```

To build in release mode, use `-configuration` option:

```bash
xcodebuild -project build.xcodefiles/build/trivial.xcodeproj -configuration Release
```

#### 3. Running test

```bash
build/build/Release/TrivialTest
```

### Building under MSBuild (Visual Studio 2013)

#### 1. Generate project files

Generate visual studio project files:

```bat
tools/gyp/gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2013
```

If you don’t use command-prompt, an alternative method is `python gyp_main.py`:

```bash
python tools/gyp/gyp_main.py build/trivial.gyp --depth=. -f msvs -G msvs_version=2013
```

#### 2. Build

If you use the command-prompt:

```bat
set Path=C:\Program Files (x86)\MSBuild\12.0\Bin\;%PATH%
```

Debug build:

```bat
MSBuild build\trivial.sln /t:Build
```

Using `/p:Configuration` you can specify the build configuration:

```bat
MSBuild build\trivial.sln /t:Build /p:Configuration=Release
```

#### 3. Running test

```bash
build\Debug\TrivialTest
```

## Notes
If you get the following error, Python can't find `setuptools` module.
```bash
$ python setup.py install
Traceback (most recent call last):
  File "setup.py", line 7, in <module>
    from setuptools import setup
ImportError: No module named setuptools
```

You can install python modules:

```bash
curl -O http://peak.telecommunity.com/dist/ez_setup.py
python ez_setup.py
...
python setup.py install
```
