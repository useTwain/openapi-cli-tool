from setuptools import setup, find_packages

setup(
    name='openapi-cli-tool',
    description="openapi cli tool - scaffold",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    version='0.1.1',
    author="Ayaka Shimada",
    author_email='aya.a.shimada@gmail.com',
    url='https;//web.hakopako.net',
    license='MIT',
    install_requires=open('requirements.txt').readlines(),
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'openapi-cli-tool = src.main:main',
        ],
    },
    zip_safe=False
)