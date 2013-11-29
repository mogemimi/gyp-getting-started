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

Second, run setup.py:

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
$ gyp build/trivial.gyp --depth=. -f xcode -D target_arch=ia32
$ gyp build/trivial.gyp --depth=. -f xcode -D target_arch=x64
```

#### 2. Build (Release/Debug)

```
$ xcodebuild -project build/trivial.xcodeproj
```

To build in release mode, use -configuration option:

```
$ xcodebuild -project build/trivial.xcodeproj -configuration Release
```

#### 3. Running test

```
$ build/build/Release/TrivialTest 
Hello, GYP
```

### Building under MSBuild (Visual Studio 2012)

#### 1. Generate project files

Generate visual studio project files: 

```
$ python tools/gyp/gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2012 -D target_arch=ia32
```

Target architecture x64:

```
$ python tools/gyp/gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2012 -D target_arch=x64
```

#### 2. Build

If you use the command-prompt:

```
$ set Path=C:\Windows\Microsoft.NET\Framework\v4.0.30319;%PATH%
```

Debug build:  

```
$ MSBuild.exe build\trivial.sln
```

Release build:  

```
$ MSBuild.exe build\trivial.sln /p:Configuration=Release
```
