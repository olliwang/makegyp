{
    'includes': [
        '../common.gypi',
    ],
    'targets': [
        {
            'target_name': 'test',
            'type': 'executable',
            'sources': [
                'test.cc',
            ],
            'dependencies': [
                'gyp_deps/boost/boost.gyp:libboost_regex',
            ],
        },
    ],
}