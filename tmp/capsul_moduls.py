from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="fileDefault" type="string" doc=""/>
	<input name="extension" type="string" doc=""/>
	<input name="title" type="string" doc=""/>
	<return name="filePath" type="file" doc=""/>
</process>
''')
def Choose_file(fileDefault, extension, title):
	listInputs=dict(zip(('fileDefault', 'extension', 'title'),(fileDefault, extension, title)))
	return cs.Choose_file(**listInputs).filePath()

@xml_process('''
<process capsul_xml="2.0">
	<input name="comment" type="string" doc=""/>
	<input name="inPath" type="file" doc=""/>
</process>
''')
def Print_Path(comment, inPath):
	listInputs=dict(zip(('comment', 'inPath'),(comment, inPath)))
	return cs.Print_Path(**listInputs)

