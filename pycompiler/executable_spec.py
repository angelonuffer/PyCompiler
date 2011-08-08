import unittest
from should_dsl import should
from executable import Function, Section, Executable


class TestFunction(unittest.TestCase):

    def it_has_a_name(self):
        Function("_start").name |should| equal_to("_start")

    def it_has_instructions(self):
        function = Function(".text")
        function.mov("rax", 42)
        function |should| have(1).instructions
        function.instructions |should| include("\tmov\trax, 42")

    def it_is_structured_text(self):
        function = Function("foo")
        function.mov("rax", 1)
        str(function) |should| equal_to("foo:\n\tmov\trax, 1\n\tret")


class TestSection(unittest.TestCase):

    def it_has_a_name(self):
        Section(".text").name |should| equal_to(".text")

    def it_has_instructions(self):
        section = Section(".text")
        section.global_("_start")
        section |should| have(1).instructions
        section.instructions |should| include("\tglobal\t_start")

    def it_has_functions(self):
        section = Section(".text")
        function = section.new_function("_start")
        section |should| have(1).functions
        section.functions |should| include(function)

    def it_is_structured_text(self):
        section = Section(".text")
        section.global_("_start")
        section.new_function("_start")
        section.new_function("write")
        str(section) |should| equal_to("section .text\n\tglobal\t_start\n_start:\n\n\tret\nwrite:\n\n\tret")


class TestExecutable(unittest.TestCase):

    def it_has_sections(self):
        executable = Executable()
        text = executable.new_section(".text")
        executable |should| have(1).sections
        data = executable.new_section(".data")
        executable |should| have(2).sections
        executable.sections |should| include(text)
        executable.sections |should| include(data)

    def it_is_structured_text(self):
        executable = Executable()
        text = executable.new_section(".text")
        text.new_function("_start")
        str(executable) |should| equal_to("section .text\n\n_start:\n\n\tret")
