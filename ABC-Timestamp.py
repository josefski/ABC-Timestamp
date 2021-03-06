#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Fri Jan 18 18:33:35 2013

import wx
import time
from time import strftime

advance=[]
times_of_day=[]
ant_beh_con=[]

# begin wxGlade: extracode
# end wxGlade


class MyDialog1(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog1.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.Student_Name = wx.TextCtrl(self, -1, "Enter Student Name Here")
        self.about = wx.Button(self, -1, "About")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "Enter Your Name Here")
        self.button_4 = wx.Button(self, -1, "OK")
        self.antecedent = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE | wx.TE_LINEWRAP | wx.TE_WORDWRAP)
        self.stamp_1 = wx.Button(self, -1, "R\ne\nc\no\nr\nd")
        self.behavior = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE | wx.TE_LINEWRAP | wx.TE_WORDWRAP)
        self.stamp_2 = wx.Button(self, -1, "R\ne\nc\no\nr\nd")
        self.consequence = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE | wx.TE_LINEWRAP | wx.TE_WORDWRAP)
        self.stamp_3 = wx.Button(self, -1, "R\ne\nc\no\nr\nd\n")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
 
        #BINDINGS There is a string that changes the binding for button_4 in input_tx. It repurposes button_4 to a save/quit button to 
        #kill the application
        self.Bind(wx.EVT_BUTTON, self.input_tx, self.stamp_1)
        self.Bind(wx.EVT_BUTTON, self.input_tx_1, self.stamp_2)
        self.Bind(wx.EVT_BUTTON, self.input_tx_2, self.stamp_3)
        self.Bind(wx.EVT_BUTTON, self.header, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.OnAboutBox, self.about)

        
    
    def __set_properties(self):
        # begin wxGlade: MyDialog1.__set_properties
        self.SetTitle("ABC Timestamp")
        self.SetSize((500, 300))
        self.Student_Name.SetMinSize((410, 27))
        self.text_ctrl_1.SetMinSize((410, 27))
        self.antecedent.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.antecedent.SetForegroundColour(wx.Colour(76, 76, 76))
        self.antecedent.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.antecedent.SetFocus()
        self.stamp_1.SetMinSize((25, 239))
        self.stamp_2.SetMinSize((25, 29))
        self.stamp_3.SetMinSize((25, 239))
        # end wxGlade
        self.behavior.Enable(False)
        self.consequence.Enable(False) 
        self.stamp_2.Enable(False)
        self.stamp_3.Enable(False) 
        
    def __do_layout(self):
        # begin wxGlade: MyDialog1.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.Student_Name, 0, 0, 0)
        sizer_2.Add(self.about, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_3.Add(self.text_ctrl_1, 0, 0, 0)
        sizer_3.Add(self.button_4, 0, 0, 0)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_5.Add(self.antecedent, 1, wx.ALL | wx.EXPAND, 1)
        sizer_5.Add(self.stamp_1, 0, wx.EXPAND, 0)
        sizer_5.Add(self.behavior, 1, wx.ALL | wx.EXPAND, 1)
        sizer_5.Add(self.stamp_2, 0, wx.EXPAND, 0)
        sizer_5.Add(self.consequence, 1, wx.ALL | wx.EXPAND, 1)
        sizer_5.Add(self.stamp_3, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_5, 1, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade


    def header(self, event, **dialogOptions): 
        #Open a "save as" dialog
        dialog = wx.DirDialog(self, **dialogOptions)
        if dialog.ShowModal() == wx.ID_OK: 
            self.dirname = dialog.GetPath()
        dialog.Destroy()  
        directory = self.dirname 
        
        #Get the names of the observer and the student from the text fields
        name=self.Student_Name.GetValue()
        observer=self.text_ctrl_1.GetValue()  
        
        #disable the text fields
        self.Student_Name.Enable(False)
        self.text_ctrl_1.Enable(False)  
        
        #Change some bindings and shut off the quit button
        self.Bind(wx.EVT_BUTTON, self.save_close, self.button_4)
        self.button_4.SetLabel("Quit") 
        self.button_4.Enable(False) 
        
        #open the text file where we'll put all the html/css this generates
        text_file = open("%s/%s.html" % (directory, name), "w")
        text_file.write("<html>\n <head>\n <style>\n")
        text_file.write('''body{
            width: 100%;
            margin: 0;
            float: none;
            background: #fff url(none);
            font: lem Georgia, "Times New Roman", Time, serif;
            color: #000;
	
            }
            table{
                border: 1px solid black;
                border-collapse: collapse;
                width: 100%;
                margin: 0;
                float: none;
                font: lem Georgia, "Times New Roman", Time, serif;
                
            }
            th.time{
                border: 1px solid black;
                border-collapse: collapse;
                width: 10%;
                margin: 0;
                float: none;
                font: lem Georgia, "Times New Roman", Time, serif;
            }
            td.time{
                border-bottom: none;
                border-collapse: collapse;
                width: 33%;
                margin: 0;
                float: none;
                font: lem Georgia, "Times New Roman", Time, serif;
                font-style: italic;
                font-size: 85%;
                }
            th{
                border: 1px solid black;
                border-collapse: collapse;
                width: 33%;
                margin: 0;
                float: none;
                font: lem Georgia, "Times New Roman", Time, serif;
                }
            td{
                border: 1px solid black;
                border-collapse: collapse;
                width: 33%;
                margin: 0;
                float: none;
                font: lem Georgia, "Times New Roman", Time, serif;
                }
            table.head{
                border: none;
                border-collapse: collapse;
                width: 100%;
                margin: 5px;
                font: lem Georgia, "Times New Roman", Time, serif;
                font-style: bold;
                }
            td.head{
                border: none;
                border-collapse: collapse;
                margin: 2;
                }

            /*p{
                padding: 2px 1px 0px 1px;
                line-height: 20%;
                }*/
                
            </style>''')

        date_time = strftime("%Y-%m-%d %H:%M:%S")

        text_file.write('<br /><p>%s</p><p>%s</p><p>Observed By: %s</p>' % (date_time, name, observer))


                
        text_file.write('''<table> 
            <tr>
            <th>Antecedent</th><th>Behavior</th><th>Consequence</th> 
            </tr> 

            ''')
    
    def input_tx(self, event):
        #Disable the quit button
        self.button_4.Enable(False) 
        
        tod = strftime("%H:%M:%S")#get the time of day  
        times_of_day.append(tod)#stick it in a list
        ant=self.antecedent.GetValue()#get the text the user entered
        ant_beh_con.append(ant)#Stick that in a list
        
        #Shade different boxes out, make it as easy as possible to navigate with the tab key
        self.antecedent.Enable(False)
        self.behavior.Enable(True)
        self.consequence.Enable(False)
        self.stamp_1.Enable(False)
        self.stamp_2.Enable(True)
        self.stamp_3.Enable(False)
        self.behavior.SetFocus()#This is necessary to make sure the cursor appears inside the text control
        
        
        
           
    def input_tx_1(self, event):
        tod_2 = strftime("%H:%M:%S")
        times_of_day.append(tod_2)
        beh=self.behavior.GetValue()
        ant_beh_con.append(beh)
        
        self.antecedent.Enable(False)
        self.behavior.Enable(False)
        self.consequence.Enable(True)
        self.stamp_1.Enable(False)
        self.stamp_2.Enable(False)
        self.stamp_3.Enable(True)
        self.consequence.SetFocus()
         
        
    def input_tx_2(self, event):
        #Re Enable the quit button
        self.button_4.Enable(True)
        
        tod_3 = strftime("%H:%M:%S")
        times_of_day.append(tod_3)
        con=self.consequence.GetValue()
        ant_beh_con.append(con)
        
        self.antecedent.Enable(True)
        self.behavior.Enable(False)
        self.consequence.Enable(False)
        self.stamp_1.Enable(True)
        self.stamp_2.Enable(False)
        self.stamp_3.Enable(False)
        
        #Clear all the text fields before cycling back around
        self.antecedent.Clear()
        self.consequence.Clear()
        self.behavior.Clear()
        
        #Go back to the first text box
        self.antecedent.SetFocus()

        #gets all the values, appends everything to the text file
        
        
        name=self.Student_Name.GetValue()#This method feels clumsy. It works in this instance, though. 
        directory=self.dirname 
        text_file = open("%s/%s.html" % (directory, name), "a")
        
        #These have to be pulled from the list in reverse order, because the pop function pops from the end of the list by 
        #default. 
        t3=times_of_day.pop()
        t2=times_of_day.pop()
        t1=times_of_day.pop()
        c=ant_beh_con.pop()
        b=ant_beh_con.pop()
        a=ant_beh_con.pop()
        text_file.write('<tr>') 
        text_file.write('<td class="time">%s</td><td class="time">%s</td><td class="time">%s</td>\n</tr>' % (t1, t2, t3)) 
        text_file.write('\n<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (a, b, c)) 

    def save_close(self, event): 
        self.Close(True) 
        self.Destroy() #Don't just leave it running. 
        
    def OnAboutBox(self, e):
        
        description = """ABC-Timestamp doesn't make it any easier to do an ABC observation. What it does do
        is create an html table in a printer friendly format that timestamps each event as you record it. 
        Sometimes it's just nice to know when something happened during an observation. This software could certainly have
        been written better. I'm not smart enough to do that, though. So if you have any suggestions, please email me.    
"""

        licence = """ABC-Timestamp is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."""


        info = wx.AboutDialogInfo()

        
        info.SetName('ABC-Timestamp')
        info.SetVersion('1.0')
        info.SetDescription(description)
        info.SetCopyright('(C) 2013 Josef Hoffman')
        info.SetWebSite('http://www.puddletownindie.com')
        info.SetLicence(licence)
        info.AddDeveloper('Josef Hoffman')
        info.AddDocWriter('Josef Hoffman')
        

        wx.AboutBox(info)

# end of class MyDialog1
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    dialog_1 = MyDialog1(None, -1, "")
    app.SetTopWindow(dialog_1)
    dialog_1.Show()
    app.MainLoop()
