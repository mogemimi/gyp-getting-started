{
  'includes': ['common.gypi'],
  'make_global_settings': [
    ['CXX','/usr/bin/clang++'],
    ['LINK','/usr/bin/clang++'],
  ],
  'target_defaults': {
    'msbuild_settings': {
      'ClCompile': {
        'WarningLevel': 'Level4', # /W4
      },
    },
    'xcode_settings': {
      'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++0x',
      'MACOSX_DEPLOYMENT_TARGET': '10.8', # OS X Deployment Target: 10.8
      'CLANG_CXX_LIBRARY': 'libc++', # libc++ requires OS X 10.7 or later
    },
  },
  'targets': [
    {
      'target_name': 'trivial_engine',
      'product_name': 'TrivialEngine',
      'type': 'static_library',
      'include_dirs': [
        '../include',
      ],
      'sources': [
        '../src/Entity.cpp',
      ],
      'xcode_settings': {
        'GCC_INLINES_ARE_PRIVATE_EXTERN': 'YES', # '-fvisibility-inlines-hidden'
        'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # '-fvisibility=hidden'
      },
    },
    {
      'target_name': 'trivial_test',
      'product_name': 'TrivialTest',
      'type': 'executable',
      'dependencies': [
        'trivial_engine',
      ],
      'include_dirs': [
        '../include',
      ],
      'sources': [
        '../test/EntityTest.cpp',
      ],
      'xcode_settings': {
      },
    },
  ] # targets
}
