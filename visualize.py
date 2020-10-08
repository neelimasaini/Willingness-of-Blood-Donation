import os
from shutil import copy,rmtree
import matplotlib.pyplot as plt

jumbocard_main = open('dependencies/jumbocard.html').read()


frame_main = open('dependencies/viz_test_frame.html').read()


card_main = open('dependencies/card.html').read()


table_main = open('dependencies/table.html').read()


class visualizer:
	global frame_main
	filecontent = frame_main
	imagecounter = 0
	#def create_output_image(self,plt):
		#print('filename is: ')
	#	fig1 = plt.gcf()
		#plt.show()
		#plt.draw()
	#	imagecounter+=1
	#	fig1.savefig('output/img/'+str(imagecounter)+'.png', dpi=100)
		
		#copy(os.getcwd()+'\\'+filename, os.getcwd()+'\\'+'output\\img\\'+str(imagecounter)+'.png')
	def __init__(self):
		try:
			rmtree('output')
		except:
			pass
		os.mkdir('output')
		os.mkdir('output/img')


		copy(os.getcwd()+'\\'+'dependencies\\pyviz.png', os.getcwd()+'\\'+'output\\img\\')
	def get_index(self):
		
		#print('File CONTENT IS: ',self.filecontent,' This')
		return self.filecontent.index('<!--561999InsertContent-->')


	def jumbocard(self,Title  ="", ImageObject = "", Description = ""):
		global jumbocard_main
		jumbocard_content = jumbocard_main
		print('Accepted: ',Title,Description)
		

		fig1 = ImageObject.gcf()
		self.imagecounter+=1
		fig1.savefig('output/img/'+str(self.imagecounter)+'.png', dpi=100)
		ImageSource = 'img/'+str(self.imagecounter)+'.png'
		print('Saving Image as: ',ImageSource)
		jumbocard_content = jumbocard_content.replace('#Title',Title)
		jumbocard_content =jumbocard_content.replace('#ImageSource',ImageSource)
		jumbocard_content =jumbocard_content.replace('#Description',Description)
		insert_at = self.get_index()
		#print('insert_at is : ',insert_at)
		self.filecontent = self.filecontent[:insert_at]+jumbocard_content+self.filecontent[insert_at:]
		#return jumbocard_content


	def card(self,Title  ="", Subtitle = "", Description = ""):
		global card_main
		card_content = card_main
		print('Accepted: ',Title,Subtitle,Description)
		
		card_content = card_content.replace('#Title',Title)
		card_content =card_content.replace('#Subtitle',Subtitle)
		card_content =card_content.replace('#Description',Description)

		insert_at = self.get_index()
		#print('insert_at is : ',insert_at)
		self.filecontent = self.filecontent[:insert_at]+card_content+self.filecontent[insert_at:]
		#return card_content


	def rendertable(self,Title = "", Content = ""):
		k= Content.split('\n')
		print('Accepted: ',Title,Content)
		main_list = []

		for x in k:
		    to_append = [y for y in x.split(' ') if y!='']
		    if not to_append== []:
		        main_list.append([y for y in x.split(' ') if y!=''])
		
		final_list = []
		for iterator in range(len(main_list)):
		    demolist = []
		    demolist = main_list[iterator]
		    if iterator == 0:
		        demolist.insert(0,'#')
		    elif iterator ==3:
		        demolist.insert(1,'#')
		        demolist.insert(1,'#')
		    elif iterator == 4 or iterator ==5:
		        demolist = []
		        demolist.append(main_list[iterator][0]+ ' '+main_list[iterator][1])
		        demolist.extend(main_list[iterator][2:])
		    final_list.append(demolist)
		

		colheads = '''<th scope="col">#Value</th>'''


		header = ''
		
		for i in final_list[0]:
			header = header+colheads.replace('#Value',i)

		#print('Header: ',header)


		prebody = ''
		cells = '''<td>#Value</td>'''
		for k in final_list[1:]:
			body=''
			for u in k:
				body = body+cells.replace('#Value',u)
			prebody = prebody + '<tr>' + body + '</tr>'

		global table_main
		table_content = table_main
		table_content = table_content.replace('#Title',Title)
		table_content = table_content.replace('#Head',header)
		table_content = table_content.replace('#Body',prebody)
		insert_at = self.get_index()
		self.filecontent = self.filecontent[:insert_at]+table_content+self.filecontent[insert_at:]

		#print(table_content)

	def generate_output(self):
		file = open('output/visual_output.html','w')
		file.write(self.filecontent)
		file.close()
		return 'Output Creation Success'