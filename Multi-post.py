...
import hashlib
^
------------------------------------------------------------

/storage/emulated/0/Multi-post.py:1:0: 'Multi-post' is not a valid module name
Traceback (most recent call last):
  File "/data/data/com.termux/files/usr/bin/cythonize", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.11/site-packages/Cython/Build/Cythonize.py", line 251, in main
    _cython_compile_files(all_paths, options)
  File "/data/data/com.termux/files/usr/lib/python3.11/site-packages/Cython/Build/Cythonize.py", line 67, in _cython_compile_files
    ext_modules = cythonize(
                  ^^^^^^^^^^
  File "/data/data/com.termux/files/usr/lib/python3.11/site-packages/Cython/Build/Dependencies.py", line 1154, in cythonize
    cythonize_one(*args)
  File "/data/data/com.termux/files/usr/lib/python3.11/site-packages/Cython/Build/Dependencies.py", line 1321, in cythonize_one
    raise CompileError(None, pyx_file)
Cython.Compiler.Errors.CompileError: /storage/emulated/0/Multi-post.py