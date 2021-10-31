# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar 13 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frmMain
###########################################################################

class frmMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"QEMU Graphical Launcher", pos = wx.DefaultPosition, size = wx.Size( 400,435 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bxsMain = wx.BoxSizer( wx.VERTICAL )
		
		fgsImages = wx.FlexGridSizer( 6, 3, 0, 0 )
		fgsImages.SetFlexibleDirection( wx.BOTH )
		fgsImages.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cbxTerm = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbxTerm.SetValue(True) 
		fgsImages.Add( self.cbxTerm, 0, wx.ALL, 5 )
		
		self.lblTerm = wx.StaticText( self, wx.ID_ANY, u"Terminal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTerm.Wrap( -1 )
		fgsImages.Add( self.lblTerm, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.txtTerm = wx.TextCtrl( self, wx.ID_ANY, u"xterm -e", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.txtTerm.SetMinSize( wx.Size( 300,-1 ) )
		
		fgsImages.Add( self.txtTerm, 0, wx.ALL, 5 )
		
		self.cbxHDD1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbxHDD1.SetValue(True) 
		fgsImages.Add( self.cbxHDD1, 0, wx.ALL, 5 )
		
		self.lblHDD1 = wx.StaticText( self, wx.ID_ANY, u"Pri HDD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblHDD1.Wrap( -1 )
		fgsImages.Add( self.lblHDD1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.fpcHDD1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_USE_TEXTCTRL )
		self.fpcHDD1.SetMinSize( wx.Size( 300,-1 ) )
		self.fpcHDD1.SetMaxSize( wx.Size( 500,-1 ) )
		
		fgsImages.Add( self.fpcHDD1, 0, wx.ALL, 5 )
		
		self.cbxHDD2 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgsImages.Add( self.cbxHDD2, 0, wx.ALL, 5 )
		
		self.lblHDD2 = wx.StaticText( self, wx.ID_ANY, u"Sec HDD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblHDD2.Wrap( -1 )
		self.lblHDD2.Enable( False )
		
		fgsImages.Add( self.lblHDD2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.fpcHDD2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_USE_TEXTCTRL )
		self.fpcHDD2.Enable( False )
		self.fpcHDD2.SetMinSize( wx.Size( 300,-1 ) )
		
		fgsImages.Add( self.fpcHDD2, 0, wx.ALL, 5 )
		
		self.cbxROM1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgsImages.Add( self.cbxROM1, 0, wx.ALL, 5 )
		
		self.lblROM1 = wx.StaticText( self, wx.ID_ANY, u"Pri ROM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblROM1.Wrap( -1 )
		self.lblROM1.Enable( False )
		
		fgsImages.Add( self.lblROM1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.fpcROM1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_USE_TEXTCTRL )
		self.fpcROM1.Enable( False )
		self.fpcROM1.SetMinSize( wx.Size( 300,-1 ) )
		
		fgsImages.Add( self.fpcROM1, 0, wx.ALL, 5 )
		
		self.cbxROM2 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgsImages.Add( self.cbxROM2, 0, wx.ALL, 5 )
		
		self.lblROM2 = wx.StaticText( self, wx.ID_ANY, u"Sec ROM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblROM2.Wrap( -1 )
		self.lblROM2.Enable( False )
		
		fgsImages.Add( self.lblROM2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.fpcROM2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_USE_TEXTCTRL )
		self.fpcROM2.Enable( False )
		self.fpcROM2.SetMinSize( wx.Size( 300,-1 ) )
		
		fgsImages.Add( self.fpcROM2, 0, wx.ALL, 5 )
		
		self.cbxFDD = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgsImages.Add( self.cbxFDD, 0, wx.ALL, 5 )
		
		self.lblFDD = wx.StaticText( self, wx.ID_ANY, u"FDD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFDD.Wrap( -1 )
		self.lblFDD.Enable( False )
		
		fgsImages.Add( self.lblFDD, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.fpcFDD = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_USE_TEXTCTRL )
		self.fpcFDD.Enable( False )
		self.fpcFDD.SetMinSize( wx.Size( 300,-1 ) )
		
		fgsImages.Add( self.fpcFDD, 0, wx.ALL, 5 )
		
		
		bxsMain.Add( fgsImages, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgSToggles = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSToggles.SetFlexibleDirection( wx.BOTH )
		fgSToggles.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.cbxChroot = wx.CheckBox( self, wx.ID_ANY, u"Chroot GNU/Linux VM", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSToggles.Add( self.cbxChroot, 0, wx.ALL, 5 )
		
		self.cbxMouse = wx.CheckBox( self, wx.ID_ANY, u"Use USB Mouse, not Tablet Device", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSToggles.Add( self.cbxMouse, 0, wx.ALL, 5 )
		
		self.cbxIDE = wx.CheckBox( self, wx.ID_ANY, u"Use IDE for disks, not VirtIO", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSToggles.Add( self.cbxIDE, 0, wx.ALL, 5 )
		
		self.cbxQXL = wx.CheckBox( self, wx.ID_ANY, u"Use QXL/SPICE instead of VNC", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSToggles.Add( self.cbxQXL, 0, wx.ALL, 5 )
		
		self.cbxSecVirtIO = wx.CheckBox( self, wx.ID_ANY, u"Use VirtIO for Sec HDD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbxSecVirtIO.Enable( False )
		
		fgSToggles.Add( self.cbxSecVirtIO, 0, wx.ALL, 5 )
		
		
		bxsMain.Add( fgSToggles, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgsNumbers = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgsNumbers.SetFlexibleDirection( wx.BOTH )
		fgsNumbers.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lblRAM = wx.StaticText( self, wx.ID_ANY, u"Memory Allocation for VM (in MiB):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblRAM.Wrap( -1 )
		fgsNumbers.Add( self.lblRAM, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.spnRAM = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, 0, 99998, 512 )
		fgsNumbers.Add( self.spnRAM, 0, wx.ALIGN_RIGHT|wx.ALL|wx.RIGHT, 5 )
		
		self.lblXPort = wx.StaticText( self, wx.ID_ANY, u"X11 listening port for remote viewer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblXPort.Wrap( -1 )
		fgsNumbers.Add( self.lblXPort, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.spnXPort = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, 0, 99, 50 )
		fgsNumbers.Add( self.spnXPort, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bxsMain.Add( fgsNumbers, 1, wx.ALIGN_CENTER, 5 )
		
		bxsButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAbout = wx.Button( self, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		bxsButtons.Add( self.btnAbout, 0, wx.ALL, 5 )
		
		self.btnLaunchVM = wx.Button( self, wx.ID_ANY, u"Launch VM", wx.DefaultPosition, wx.DefaultSize, 0 )
		bxsButtons.Add( self.btnLaunchVM, 0, wx.ALL, 5 )
		
		self.btnExit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bxsButtons.Add( self.btnExit, 0, wx.ALL, 5 )
		
		
		bxsMain.Add( bxsButtons, 1, wx.ALIGN_CENTER, 5 )
		
		
		self.SetSizer( bxsMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cbxTerm.Bind( wx.EVT_CHECKBOX, self.runToggleTerm )
		self.cbxTerm.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.txtTerm.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxHDD1.Bind( wx.EVT_CHECKBOX, self.runToggleChroot )
		self.cbxHDD1.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.fpcHDD1.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxHDD2.Bind( wx.EVT_CHECKBOX, self.runToggleDrives )
		self.cbxHDD2.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.fpcHDD2.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxROM1.Bind( wx.EVT_CHECKBOX, self.runToggleDrives )
		self.cbxROM1.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.fpcROM1.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxROM2.Bind( wx.EVT_CHECKBOX, self.runToggleDrives )
		self.cbxROM2.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.fpcROM2.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxFDD.Bind( wx.EVT_CHECKBOX, self.runToggleDrives )
		self.cbxFDD.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.fpcFDD.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxChroot.Bind( wx.EVT_CHECKBOX, self.runToggleControls )
		self.cbxChroot.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxMouse.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxIDE.Bind( wx.EVT_CHECKBOX, self.runToggleSecVirtIO )
		self.cbxIDE.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxQXL.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.cbxSecVirtIO.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.spnRAM.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.spnXPort.Bind( wx.EVT_KILL_FOCUS, self.runSaveConfig )
		self.btnAbout.Bind( wx.EVT_BUTTON, self.runAboutDialog )
		self.btnLaunchVM.Bind( wx.EVT_BUTTON, self.runLaunchVM )
		self.btnExit.Bind( wx.EVT_BUTTON, self.runExitApp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def runToggleTerm( self, event ):
		event.Skip()
	
	def runSaveConfig( self, event ):
		event.Skip()
	
	
	def runToggleChroot( self, event ):
		event.Skip()
	
	
	
	def runToggleDrives( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	def runToggleControls( self, event ):
		event.Skip()
	
	
	
	def runToggleSecVirtIO( self, event ):
		event.Skip()
	
	
	
	
	
	
	def runAboutDialog( self, event ):
		event.Skip()
	
	def runLaunchVM( self, event ):
		event.Skip()
	
	def runExitApp( self, event ):
		event.Skip()
	

###########################################################################
## Class frmAbout
###########################################################################

class frmAbout ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"About QGL", pos = wx.DefaultPosition, size = wx.Size( 300,410 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_FLOAT_ON_PARENT|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"qgl.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_bitmap1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_bitmap1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer16.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Version 1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		self.m_staticText16.SetFont( wx.Font( 18, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer16.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"QEMU Graphical Launcher is an application designed for simple QEMU virtual machine management.\n\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText20.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText20.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer16.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"© 2015 Paul A. Hinchberger III", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText18.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText18.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer16.Add( self.m_staticText18, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details at http://www.gnu.org/licenses/.\n\n\n\n\n\n\n", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 8, 70, 90, 90, False, wx.EmptyString ) )
		self.m_staticText19.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText19.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer16.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer16 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

