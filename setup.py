from os import path,listdir,system
import setuptools

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='hydralit_components',
    version='1.0.10',
    description='Components to use with or without the Hydralit package.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tanglespace/hydralit_components',
    author='Jackson Storm',
    author_email='c6lculus8ntr0py@gmail.com',
    include_package_data=True,
    license="Apache 2",
    project_urls={
        'Documentation': 'https://github.com/tanglespace/hydralit_components',
        'Source': 'https://github.com/tanglespace/hydralit_components',
        'Tracker': 'https://github.com/tanglespace/hydralit_components/issues',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    install_requires=[
        'streamlit>=1.7',
        'lxml',
        'bs4'
    ],
    python_requires='>=3.6',
    keywords=[
        'Streamlit',
        'Web',
        'Responsive',
        'Deployment',
        'Web Application',
        'Presentation',
    ],
)
