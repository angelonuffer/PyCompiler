class Function(object):

    def __init__(self, name):
        self.name = name
        self.instructions = []
        self._instruction = ""

    def __getattr__(self, instruction):
        self._instruction = instruction.strip("_")
        return self

    def __call__(self, *args):
        args = map(str, args)
        self.instructions.append("\t%s\t%s" % (self._instruction, ", ".join(args)))
        self._instruction = ""

    def __str__(self):
        return "%s:\n%s\n\tret" % (self.name, "\n".join(self.instructions))


class Section(object):

    def __init__(self, name):
        self.name = name
        self.instructions = []
        self._instruction = ""
        self.functions = []

    def __getattr__(self, instruction):
        self._instruction = instruction.strip("_")
        return self

    def __call__(self, *args):
        args = map(str, args)
        self.instructions.append("\t%s\t%s" % (self._instruction, ", ".join(args)))
        self._instruction = ""

    def __str__(self):
        return "section %s\n%s\n%s" % (self.name, "\n".join(self.instructions), "\n".join(map(str, self.functions)))

    def new_function(self, name):
        function = Function(name)
        self.functions.append(function)
        return function


class Executable(object):

    def __init__(self):
        self.sections = []

    def __str__(self):
        return "\n".join(map(str, self.sections))

    def new_section(self, name):
        section = Section(name)
        self.sections.append(section)
        return section
