"""CP1404 Practical - Languages
Estimated: 30 minutes
Current time: 16:54
Finish time:
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python, ruby, visual_basic]

print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)