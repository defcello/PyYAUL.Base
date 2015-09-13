Uniform code styling is vital to good, maintainable code!  I have my own minute rules that I follow,
but these are the big ones.

# Indentation
4 spaces.  NO TABS!  I'm more fond of 2 spaces, but since this is public-facing I'm going to stick
with 4.

# Max Width
100 chars.

# "__init__.py" files
NO.  NEVER.  JUST SAY NO TO DRUGS.  In short, it destroys code traceability, rends implicit
namespace packages, and brings with it a lot of bad habits ("__all__" anyone?).  With Implicit
Namespace Modules, we are finally rid of this disease of a file and can reap the benefits of a more
flexible import namespace where packages may span multiple locations in the file system!  The only
exception is if you are explicitly trying to break the import system, such as what we have done with
the "__init__.py" file located in the root folder of the source code to prevent users from
installing the library improperly and risking double-imports and code that doesn't run.

# `from super.awesome.module import *`
EVERY TIME YOU TYPE THIS A PUPPY DIES!  YOU MONSTER.  Seriously, this destroys code traceability.
If someone is looking through your code (e.g. your future self), they should be able to trace every
single variable to its definition with a simple in-file word search.  If you use `import *`, what
would have been at worst a `sys.modules` query (to figure out the origin of the "from" target
module) just became a project-wide file search, especially if you called an "import *" on an
"__init__.py" file that had its own "import *" statements.  Let's hope that variable is only defined
once in the whole project!  THINK OF THE PUPPIES!

# Naming Conventions
## Files/Modules/Directories
Python modules and directories--specifically any file/directory subject to being in a Python import
path--shall be named using all lowercase letters and NO UNDERSCORES.  Fight that urge to delimit
words in the module name!  It's not necessary and just looks tacky next to stock Python's clean
import paths.

## Classes
Classes shall be named using Title Case.  Acronyms are treated as multiple words such that each
letter signifying the start of a word is capitalized.  Examples:
 - MyClass
 - MyXMLParser

## Functions and Variables
Functions shall be named using camel Case.  Acronyms are treated the same as they are in classes
(all uppercase) except when the abbreviation starts the function name, in which case it is treated
as a single word where all letters are lowercase.  Examples:
 - myVar
 - htmlFilePath
An exception to this rule is any variable that stores what would be considered constants, such as
enum values.  Such "constant" variables shall be named all uppercase.

# Code documentation.
Sphinx for generating API documentation.  Examples available at
"https://pythonhosted.org/an_example_pypi_project/sphinx.html".

ALL FUNCTIONS, CLASSES, MODULES, MODULE VARIABLES, AND CLASS VARIABLES MUST BE DOCUMENTED!  The
exception is if that item is already documented in a subclass.

# Unit testing.
Unit testing is good.  Use it.  When you add a new module/class/function, go to its respective
"_test/test<modulename>.py" file (creating one if not already existing) and add test code for it.

Feeling lazy?  Consider this:

# You have to determine your code is functional before pushing.
  * Pushing untested code is reckless.  We've all done it, I can say I almost always regret it.
# Get out of the habit of testing your code manually.
  * "But DefCello, all I have to do is import it through Python interactive mode and run a few
    commands!  Why should I go through the effort of writing a whole unit test for it!  Plus, it
    could change in the future and unit tests will have to be changed.  They become maintenance
    problems!"  Sure, it might be faster to go manual the FIRST time, but what about all that time
    wasted doing all that typing/copy-paste work the SECOND, or THIRD, or FOURTH time?
    Collectively, it's much faster to write the automated test up front and then implement the
    functionality until the test passes (Test-Driven Development--it works!).  And that's not even
    factoring in standard benefits of catching unexpected changes, making maintenance work where
    interfaces don't change a painless process, and helping other people and your future self
    understand how your snazzy class/function is supposed to be used.  Sure, that feature could
    change in the future, possibly requiring a full rewrite of the unit tests, but that's for future
    developers to worry about.  Your focus is on the code you're committing NOW that's supposed to
    work NOW, and all the typing/copy-paste work you're saving yourself by just doing it automated
    right from the get-go.
