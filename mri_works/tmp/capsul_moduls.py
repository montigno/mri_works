from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="command" type="string" doc=""/>
</process>
''')
def ImageJ_execution(command,):
	listInputs=dict(zip(('command',),(command,)))
	return cs.ImageJ_execution(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="cmd_ant" type="string" doc=""/>
	<return name="cmd_post" type="string" doc=""/>
</process>
''')
def ortho_view(cmd_ant,):
	listInputs=dict(zip(('cmd_ant',),(cmd_ant,)))
	return cs.ortho_view(**listInputs).cmd_post()

@xml_process('''
<process capsul_xml="2.0">
	<input name="file" type="file" doc=""/>
	<return name="cmd_post" type="string" doc=""/>
</process>
''')
def ImageJ_load_Image(file,):
	listInputs=dict(zip(('file',),(file,)))
	return cs.ImageJ_load_Image(**listInputs).cmd_post()

@xml_process('''
<process capsul_xml="2.0">
	<input name="extension" type="string" doc=""/>
	<input name="title" type="string" doc=""/>
	<return name="filePath" type="file" doc=""/>
</process>
''')
def askopenfilename(extension, title):
	listInputs=dict(zip(('extension', 'title'),(extension, title)))
	return cs.askopenfilename(**listInputs).filePath()

