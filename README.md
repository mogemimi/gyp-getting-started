gyp-getting-started
===================

For more information, see

* [http://enginetrouble.net/2013/07/getting-started-with-gyp.html](http://enginetrouble.net/2013/07/getting-started-with-gyp.html)
* [http://enginetrouble.net/](http://enginetrouble.net/)

Feedback, issues and pull requests are always welcome, please see the [Github issues page](https://github.com/enginetrouble/gyp-getting-started/issues).

## Getting the code

```shell
git clone git://github.com/enginetrouble/gyp-getting-started.git
```

## Requirements

* Python 2.7+ (:warning: GYP does not support Python 3, at the moment)
* Xcode 5 and 6
* Visual Studio 2013

## How to build

### Prerequisite: Installing GYP

First, install GYP from https://chromium.googlesource.com/external/gyp.  
Make sure `git` is installed.
From the root of your engine directory (`cd gyp-getting-started`), run:

```shell
git clone https://chromium.googlesource.com/external/gyp.git tools/gyp
```

Second, run `setup.py`:

**Linux and Mac OSX**

To install globally with gyp:

```shell
cd tools/gyp
[sudo] python setup.py install
```

**Windows**

```shell
cd tools/gyp
python setup.py install
```

### Building under Xcode (Apple LLVM Clang++)

#### 1. Generate project

```shell
gyp build/trivial.gyp --depth=. -f xcode --generator-output=build.xcodefiles
```

#### 2. Build (Debug/Release)

```shell
xcodebuild -project build.xcodefiles/build/trivial.xcodeproj
```

To build in release mode, use `-configuration` option:

```shell
xcodebuild -project build.xcodefiles/build/trivial.xcodeproj -configuration Release
```

#### 3. Running test

```shell
build/build/Release/TrivialTest
```

### Building under MSBuild

#### 1. Generate project files

To generate visual studio project files in Windows default command prompt, run `gyp\gyp` (same as `gyp\gyp.bat`):

```bat
tools\gyp\gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2013
```

If you use Git Bash (MinGW) or Cygwin, an alternative method is `gyp/gyp` (shell script, not `.bat` file):

```shell
tools/gyp/gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2013
```

You can also use the `python gyp_main.py` instead of `gyp` command:

```shell
python tools/gyp/gyp_main.py build/trivial.gyp --depth=. -f msvs -G msvs_version=2013
```

An Visual Studio solution file (`build/trivial.sln`) has been created in your directory.

#### 2. Build using MSBuild

If you use the Visual Studio 2013, run the following in a command prompt:

```bat
set Path=C:\Program Files (x86)\MSBuild\12.0\Bin\;%PATH%
```

To compile and create an executable file, run the following command:

```bat
MSBuild build\trivial.sln /t:Build
```

Using `/p:Configuration` you can specify the build configuration:

```bat
MSBuild build\trivial.sln /t:Build /p:Configuration=Release
```

#### 3. Running test

```bat
build\Debug\TrivialTest
```

## Notes

If you get the following error, Python can't find `setuptools` module.

```shell
$ python setup.py install
Traceback (most recent call last):
  File "setup.py", line 7, in <module>
    from setuptools import setup
ImportError: No module named setuptools
```

You can install python modules and try again:

```shell
wget https://bootstrap.pypa.io/ez_setup.py -O - | python
python setup.py install
```

For more information about installing `setuptools`, please see https://pypi.python.org/pypi/setuptools#unix-wget.
