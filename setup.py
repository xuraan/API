from setuptools import setup, find_packages

setup(
    name='xuranapi',
    version='0.1',
    author='Samba Diawara',
    author_email='afrcvn@frcvn.com',
    description='A package for doing cool things',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='example package',
    install_requires=[
        'fastapi',
        'deta',
    ],
    entry_points={
        'console_scripts': [
            # 'mycommand=mypackage.command_line:main',
        ],
    },
)