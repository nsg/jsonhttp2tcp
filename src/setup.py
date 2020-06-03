import setuptools

setuptools.setup(
    name="service",
    py_modules=["service"],
    entry_points={"console_scripts": ["service=service:main"]},
)
