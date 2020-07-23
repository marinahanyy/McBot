from rivescript import RiveScript
import xlwt
import os.path
file = os.path.dirname(__file__)
book = xlwt.Workbook()
sheet = book.add_sheet("attendance sheet")
Brain = os.path.join(file, 'mybrain')
global col
r=0
col = 0

def runrive():
    bot = RiveScript(utf8=True)
    bot.load_directory('./mybrain')
    bot.sort_replies()
    while True:
        msg = input('You> ')
        if msg == 'q':
            break
        reply = bot.reply("localuser", msg)
        print('Bot>', reply)
    bot.deparse()


def toExcelN(name):

  global r
  global col
  col =0


  sheet.write(r, col, name)
  book.save("attendance.xls")
  r = r + 1
  return None


def toExcelId(id):
  col =1
  sheet.write(r-1, col, id)
  book.save("attendance.xls")

  return None

if __name__ == "__main__":
    runrive()