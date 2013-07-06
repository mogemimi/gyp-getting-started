gyp-getting-started
===================

For more information, see  
[http://enginetrouble.net/](http://enginetrouble.net/)  

## Getting the code

```
$ git clone git@github.com:enginetrouble/gyp-getting-started.git
```

## How to build

### Prerequisites

First , install GYP from https://code.google.com/p/gyp/.  
```
$ svn --version
$ svn co http://gyp.googlecode.com/svn/trunk tools/gyp tools/gyp
```  
or  
```
$ git clone git://github.com/svn2github/gyp.git tools/gyp tools/gyp
```

Second, run setup.py:

**Linux and Mac OSX:**

```
$ cd tools/gyp
$ sudo python setup.py install
```

**Windows:**

```
$ python --version
$ python setup.py install
```

### Building under Xcode (Apple LLVM Clang++)

#### Prerequisites

* GYP
* Python (version 2.x)

#### Generate project and build:

```
$ gyp build/trivial.gyp --depth=. -f xcode
$ xcodebuild -project build/trivial.xcodeproj
```

### Building under MSBuild (Visual Studio 2012)

#### Prerequisites

* GYP
* Python (version 2.x)
* Command prompt or MinGW + MSYS

#### 1. Generate project files:

Generate visual studio project files: 

```
$ python tools/gyp/gyp build/trivial.gyp --depth=. -f msvs -G msvs_version=2012
```

#### 2. Build:

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
