from capsul.process.xml import xml_process
import capsul_code_source as cs

@xml_process('''
<process capsul_xml="2.0">
	<input name="atlas_name" type="string" doc=""/>
	<return name="atlas_filename" type="file" doc=""/>
</process>
''')
def fetch_atlas_harvard_oxford(atlas_name,):
	listInputs=dict(zip(('atlas_name',),(atlas_name,)))
	return cs.fetch_atlas_harvard_oxford(**listInputs).atlas_filename()

@xml_process('''
<process capsul_xml="2.0">
	<input name="atlas_filename" type="file" doc=""/>
</process>
''')
def Plot_roi(atlas_filename,):
	listInputs=dict(zip(('atlas_filename',),(atlas_filename,)))
	return cs.Plot_roi(**listInputs)

