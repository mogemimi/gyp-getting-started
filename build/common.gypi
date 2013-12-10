{
  'variables': {
	'conditions': [
      ['OS == "mac"', {
        'target_arch%': 'x64',
      }, {
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
        'msvs_settings': {
          'VCCLCompilerTool': {
            'Optimization': '0', # /Od
            'conditions': [
              ['OS == "win" and component == "shared_library"', {
                'RuntimeLibrary': '3', # /MDd
              }, {
                'RuntimeLibrary': '1', # /MTd
              }],
            ],
          },
          'VCLinkerTool': {
            'LinkIncremental': '2',
          },
        },
        'xcode_settings': {
          'GCC_OPTIMIZATION_LEVEL': '0', # -O0
        },
      }, # Debug
      'Release': {
        'cflags': ['-O3'],
        'msvs_settings':{
          'VCCLCompilerTool': {
            'Optimization': '2', # /O2
            'InlineFunctionExpansion': '2',
            'conditions': [
              ['OS == "win" and component == "shared_library"', {
                'RuntimeLibrary': '2', # /MD
              }, {
                'RuntimeLibrary': '0', # /MT
              }],
            ],
          },
          'VCLinkerTool': {
            'LinkIncremental': '1',
            'OptimizeReferences': '2',
          },
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
