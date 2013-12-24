gyp-getting-started
===================

For more information, see  

* [http://enginetrouble.net/2013/07/getting-started-with-gyp.html](http://enginetrouble.net/2013/07/getting-started-with-gyp.html)  
* [http://enginetrouble.net/](http://enginetrouble.net/)  

## Getting the code

```
$ git clone git://github.com/enginetrouble/gyp-getting-started.git
```

## How to build

### Prerequisites

* Python (version 2.x)
* GYP

### Prerequisite: Installing GYP

First, install GYP from https://chromium.googlesource.com/external/.  
Make sure git is installed.
From the root of your engine directory, run:  
```
$ git clone https://chromium.googlesource.com/external/gyp.git tools/gyp
```

or

```
$ svn --version
$ svn co http://gyp.googlecode.com/svn/trunk tools/gyp tools/gyp
```  

Second, run `setup.py`:

**Linux and Mac OSX**

To install globally with gyp:

```
$ cd tools/gyp
$ [sudo] python setup.py install
```

**Windows**

```
$ cd tools/gyp
$ python setup.py install
```

### Building under Xcode (Apple LLVM Clang++)

#### 1. Generate project

```
$ gyp build/trivial.gyp --depth=. -f xcode --generator-output=./build.xcodefiles/
```

#### 2. Build (Debug/Release)

```
$ xcodebuild -project build.xcodefiles/build/trivial.xcodeproj
```

To build in release mode, use `-configuration` option:

```
$ xcodebuild -project build.xcodefiles/build/trivial.xcodeproj -configuration Release
```

#### 3. Running test

```
$ build/build/Release/TrivialTest 
Hello, GYP
```

### Building under MSBuild (Visual Studio 2013)

#### 1. Generate project files

Generate visual studio project files:

```
$ tools/gyp/gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2013
```

or running with `gyp_main.py`:

```
$ python tools/gyp/gyp_main.py build/trivial.gyp --depth=. -f msvs -G msvs_version=2013
```

Using `-D target_arch` you can specify the target architecture:

```
$ tools/gyp/gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2013 -D target_arch=ia32
$ tools/gyp/gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2013 -D target_arch=x64
```

#### 2. Build

If you use the command-prompt:

```
$ set Path=C:\Windows\Microsoft.NET\Framework\v4.0.30319;%PATH%
```

Debug build:  

```
$ MSBuild.exe build\trivial.sln /t:Build /toolsversion:12.0
                                /p:PlatformToolset=v120;TargetFrameworkVersion=v4.5.1
```

Release build:  

```
$ MSBuild.exe build\trivial.sln /t:Build /toolsversion:12.0
                                /p:PlatformToolset=v120;TargetFrameworkVersion=v4.5.1
                                /p:Configuration=Release
```

## Notes
If you get the following error, Python can't find `setuptools` module.
```
$ python setup.py install
Traceback (most recent call last):
  File "setup.py", line 7, in <module>
    from setuptools import setup
ImportError: No module named setuptools
```

You can install python modules:

```
$ curl -O http://peak.telecommunity.com/dist/ez_setup.py
$ python ez_setup.py
...
$ python setup.py install
```
