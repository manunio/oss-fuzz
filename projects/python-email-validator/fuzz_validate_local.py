import sys
import atheris

from email_validator.syntax import validate_email_local_part, \
        check_unsafe_chars, validate_email_domain_name, \
        validate_email_domain_name
from idna.intranges import intranges_from_list

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    try:
        # op = fdp.ConsumeIntInRange(0,2)
        # print("op: " + str(op))
        # if op == 0:
        intranges_from_list(
                list(range(fdp.ConsumeIntInRange(0,293), fdp.ConsumeIntInRange(0,499))) +
                list(range(fdp.ConsumeIntInRange(0,4888), fdp.ConsumeIntInRange(0,9876)))
            )
       
        validate_email_local_part(fdp.ConsumeString(1024), allow_smtputf8=fdp.ConsumeBool())
        # elif op == 1:
        check_unsafe_chars(fdp.ConsumeString(1024))
        # elif op == 2:
        validate_email_domain_name(fdp.ConsumeString(1024))

        print("<<- PASSED ->>>")
    except Exception as e:
       print(str(e))

def main():
   atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
   atheris.instrument_all()
   atheris.Fuzz()

if __name__ == '__main__':
    main()
