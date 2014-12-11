{
  'variables': {
	'conditions': [
      ['OS == "mac"', {
        'target_arch%': 'x64',
      }],
      ['OS == "win"', {
        'target_arch%': 'ia32',
      }],
	  ['OS != "mac" and OS != "win"', {
        'target_arch%': '<(target_arch)',
      }],
    ],
  },
  'target_defaults': {
    'default_configuration': 'Release',
	'conditions': [
      ['target_arch == "arm"', {
        # arm
      }], # target_archs == "arm"
      ['target_arch == "ia32"', {
        'xcode_settings': {
          'ARCHS': ['i386'],
        },
      }], # target_archs == "ia32"
      ['target_arch == "mipsel"', {
        # mipsel
      }], # target_archs == "mipsel"
      ['target_arch == "x64"', {
        'xcode_settings': {
          'ARCHS': ['x86_64'],
        },
      }], # target_archs == "x64"
    ],
    'configurations': {
      'Debug': {
        'defines':['DEBUG=1'],
        'cflags': ['-g', '-O0'],
        'msbuild_settings': {
          'ClCompile': {
            'Optimization': 'Disabled', # /Od
            'conditions': [
              ['OS == "win" and component == "shared_library"', {
                'RuntimeLibrary': 'MultiThreadedDebugDLL', # /MDd
              }, {
                'RuntimeLibrary': 'MultiThreadedDebug', # /MTd
              }],
            ],
          },
          'Link': {
            #'LinkIncremental': 'true', # /INCREMENTAL
          },
          #'': {
          # 'LinkIncremental': 'true', # /INCREMENTAL
          #},
        },
        'xcode_settings': {
          'GCC_OPTIMIZATION_LEVEL': '0', # -O0
        },
      }, # Debug
      'Release': {
        'cflags': ['-O3'],
        'msbuild_settings':{
          'ClCompile': {
            'Optimization': 'MaxSpeed', # /O2
            'InlineFunctionExpansion': 'AnySuitable', # /Ob2
            'conditions': [
              ['OS == "win" and component == "shared_library"', {
                'RuntimeLibrary': 'MultiThreadedDLL', # /MD
              }, {
                'RuntimeLibrary': 'MultiThreaded', # /MT
              }],
            ],
          },
          'Link': {
            #'LinkIncremental': 'false', # /INCREMENTAL:NO
            'OptimizeReferences': 'true', # /OPT:REF
          },
          #'': {
          # 'LinkIncremental': 'false', # /INCREMENTAL:NO
          #},
        },
        'xcode_settings': {
          'GCC_OPTIMIZATION_LEVEL': '3', # -O3
        },
      }, # Release
    }, # configurations
    'variables': {
      'component%': 'static_library',
    },
  }, # target_defaults
}
