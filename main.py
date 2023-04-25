import os
import oop


adress_book = oop.AddressBook()
bot_working = True
clear = lambda: os.system('clear')

#for test
a1 = oop.Name()
a1.value = 'Max'
b1 = oop.Phone()
b1.value = '12'
c1 = oop.Birthday()

a2 = oop.Name()
a2.value = 'Ann'
b2 = oop.Phone()
b2.value = '13'
c2 = oop.Birthday()
c2.value = '12-12-2001'
rec1 = oop.Record(a1,b1,c1)
rec2 = oop.Record(a2,b2,c2)

add_ph = oop.Phone()
add_ph.value = '34343434'
rec1.add_phone(add_ph)
adress_book.addRecord(rec1)
adress_book.addRecord(rec2)


def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except UnboundLocalError:
            print('Enter command')
            return func(*args,**kwargs)
        except TypeError:
            print('Enter name and phone separated by a space!')
            return func(*args,**kwargs)
        except KeyError:
            print('This name not found!')
            return func(*args,**kwargs)
        except IndexError:
            print('This name found! Enter another name.')
            return func(*args,**kwargs)
        except ValueError:
            return func(*args,**kwargs)
    return(inner)


def start():
    clear()
    print(f"CLI Address book bot is running...")


def show_page(page_number=1, count=5):
    return adress_book.show_page(page_number, count)


def helper():
    clear()
    res = ''
    for key in COMMANDS.keys():
        res += f"{key}\n"
    return "Available bot function:\n" + res


def close():
    clear()
    global bot_working
    bot_working = False
    return ("Good bye!")


def hello():
    clear()
    return ('How can I help you?')


@input_error
def add_record(name, phone='' ,birthday=''):
    clear()
    rec_name = oop.Name()
    rec_name.value = name

    rec_phone = oop.Phone()
    rec_phone.value = phone

    rec_bd = oop.Birthday()
    rec_bd.value = birthday

    rec = oop.Record(rec_name, rec_phone, rec_bd)

    adress_book.addRecord(rec)
    return rec.print_record()


def change_phone(name, old_phone, new_phone):
    clear()
    rec = adress_book[name]
    o_ph = oop.Phone()
    o_ph.value = old_phone
    n_ph = oop.Phone()
    n_ph.value = new_phone
    rec.change_phone(o_ph, n_ph)
    return rec.print_record()


def add_phone(name, phone):
    clear()
    rec = adress_book[name]
    ph = oop.Phone()
    ph.value = phone
    rec.add_phone(ph)
    return rec.print_record()


def add_birthday(name, birthday):
    clear()
    rec = adress_book[name]
    bd = oop.Birthday()
    bd.value = birthday
    rec.add_birthday(bd)
    return rec.print_record()


def delete_phone(name, phone):
    clear()
    rec = adress_book[name]
    ph = oop.Phone()
    ph.value = phone
    rec.del_phone(ph)
    return rec.print_record()


def days_to_birthday(name):
    clear()
    rec = adress_book[name]
    return rec.days_to_birthday()


def showall():
    clear()
    return adress_book.print_all()



def phone(name):
    clear()
    rec = adress_book[name]
    return rec.print_record()


def unknown_command():
    return "Unknown command, try again"


def command_parse(s):
    for key, cmd in  COMMANDS.items():
        if key in s.lower():
            return cmd, s[len(key):].strip().split()
    return unknown_command, []


COMMANDS = {'hello':hello,
            'days to bd':days_to_birthday,
            'add phone': add_phone,
            'add birthday': add_birthday,
            'change phone':change_phone,
            'delete phone': delete_phone,
            'find phone':phone,
            'show page':show_page,
            'show all':showall,
            'good bye':close,
            'exit':close,
            'close':close,
            'add': add_record,
            'help':helper,
            }


@input_error
def main():
    start()
    while bot_working:
        s = input()
        command, arguments = command_parse(s)
        print(command(*arguments))


if __name__ == '__main__':
    clear()
    main()