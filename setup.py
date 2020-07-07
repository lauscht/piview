import setuptools


setuptools.setup(
    name="PiView", # Replace with your own username
    version="0.0.1",
    author="Tobias Lausch",
    author_email="T.Lausch@pi.de",
    description="Python code for visualization of cool PI FPGA Tools",
    package_dir={'':'backend'},
    packages=['piView'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)