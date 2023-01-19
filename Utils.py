import datetime
import os
class Files:
    class Config:
        Flag = "--- Config File ---"
        def Append(Text,State):
            if os.path.exists("Config.cfg"):
                #print("debug Point 1")
                f = open("Config.cfg", "a")
                TempRead = Files.Config.ReadLine(1)
                if TempRead.__contains__(Files.Config.Flag):
                    #print("debug Point 2")
                    f.write(Text + ":"+ State +":\n")
                else:
                    f.write(Files.Config.Flag + ":\n")
                    f.write(Text + ":"+ State +":\n")
                    #print("debug Point 3")
                f.close()
                
            else:
                f = open("Config.cfg", "x")
                f.close()
                Files.Config.Append(Text,State)  


        def Dump():
            f = open("Config.cfg", "r")
            dump = f.read()
            lines = dump.split("\n")
            State = str(lines).split(":")
            f.close()
            return State

        def ReadLine(line):
            arr = Files.Config.Dump()
            output = arr[line - 1]
            return output
        def Read(Search):
            dump = Files.Config.Dump()
            for i in range(0, len(Search)):
                if (i % 2) == 1:
                    cleaned = dump[i].split("[")
                    print(cleaned[0])
                elif (i % 2) == 0:
                    cleaned = dump[i].split("'")
                    print(cleaned[0])
                i = i + 1
    def Overwrite(File):
        f = open(File, "x")
        f.close()

    def Append(File,Text):
        f = open(File, "a")
        f.write(Text + "\n")
        f.close()

    def Read(File):
        f = open(File, "r")
        dump = f.read()
        lines = dump.split("\n")
        f.close()
        return lines

    def Create(File):
        f = open(File, "a")
        f.close()

    def CsvRead(file):
        x = []
        x = Obj.split(",")
        return x

    def ReadLine(file,line):
        arr = Access.Read(file)
        return arr[line - 1]
class Print:
    def Printer(Text,PrettyPrint):
        if (PrettyPrint):
            print(" - " + Text + " - ")
        else:
            print(Text)
class Array:
    def Write(Store,Index,Data):
        print(Data)
        Store.append(Store[Index])
        Store[Index] = Data
    def Read(Store):
        print(Store)
    def Append(Store,Data):
        print(Data)
        Store.append(Data)
    def Remove(Store,Index):
        del Store[Index]
    def Clear(Store):
        Store.clear()
    def Pop(Store,Index,Data):
        Store[Index] = Data
    def Return(Store,Index):
        return Store[Index]
    def Print(Store):
        print(Data)
class Input:
    def ReadString():
        Read = str(input())
        return Read
    def ReadInt():
        Read = int(input())
        return Read
    def ReadBool():
        Read = bool(input())
        return Read
    def ReadDouble():
        Read = Decimal(input())
        return Read
    def ReadAny():
        Read = input()
        return Read
class Time:
    
    x = datetime.datetime.now()
    shortday = x.strftime("%a")
    longday = x.strftime("%A")
    day = x.strftime("%d")
    month = x.strftime("%m")
    year = x.strftime("%Y")
    hour = x.strftime("%H")
    Min = x.strftime("%M")
    shortmonthname = x.strftime("%b")
    longmonthname = x.strftime("%B")

    def GetTime():
        return(hour + ":" + Min)

    def GetDay(Text):
        if Text:
            return(longday)
        else:
            return(day)

    def GetDT():
        date = GetDate()
        time = GetTime()
        return(date + " " + time)

    def GetDate():
        return(""+day+"/"+month+"/"+year)

    def GetTime():
        return(hour + ":" + Min)

    def GetTime():
        return(hour + ":" + Min)