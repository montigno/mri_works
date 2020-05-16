from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="sourceFile" type="file" doc=""/>
	<input name="title" type="string" doc=""/>
	<input name="display_mode" type="string" doc=""/>
	<input name="dim" type="int" doc=""/>
	<input name="draw_cross" type="bool" doc=""/>
	<input name="annotate" type="bool" doc=""/>
</process>
''')
def MatPlotLib(sourceFile, title, display_mode, dim, draw_cross, annotate):
	listInputs=dict(zip(('sourceFile', 'title', 'display_mode', 'dim', 'draw_cross', 'annotate'),(sourceFile, title, display_mode, dim, draw_cross, annotate)))
	return cs.MatPlotLib(**listInputs)

@xml_process('''
<process capsul_xml="2.0">
	<input name="in_file" type="file" doc=""/>
	<input name="ref_file" type="file" doc=""/>
	<input name="invert" type="bool" doc=""/>
	<return name="out_file" type="file" doc=""/>
</process>
''')
def image_Rescale(in_file, ref_file, invert):
	listInputs=dict(zip(('in_file', 'ref_file', 'invert'),(in_file, ref_file, invert)))
	return cs.image_Rescale(**listInputs).out_file()

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

