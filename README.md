Description of the project.

This project is an Airbnb clone,Airbnb is a website for booking of shortlet houses.This project attempts to replicate it.

Description of the command interpreter
A command interpreter is used to manipulate data without a visual interface, like a shell (for development and debugging).

Files and Directories
models directory will contain all classes used for the entire project. A class, called model in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.
console.py file is the entry point of our command interpreter.
models/base_model.py file is the base class of all our models. It contains common elements:
attributes: id, created_at and updated_at
methods: save() and to_json()
