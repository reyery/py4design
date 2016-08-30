import time
import os
import pyliburo

#specify the citygml file
current_path = os.path.dirname(__file__)
parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
citygml_filepath = os.path.join(parent_path, "punggol_case_study", "citygml", "punggol_luse24.gml")
result_citygml_filepath = os.path.join(parent_path, "punggol_case_study", "citygml", "punggol_variant.gml")

time1 = time.clock()   
display_2dlist = []

parameterise = pyliburo.gmlparameterise.Parameterise(citygml_filepath)
parameterise.define_nparameters()
parameters = parameterise.generate_random_parameters()

#plot24 with 14 buildings and 40 parameters
#parameters for the figures
#parameters = [0.4015528247148732, 0.4300277431593764, 0.5206052173461907, 0.2623832368774498, 0.44963374200111683, 0.2892102590487512, 0.04684850731024537, 0.709277459826544, 0.6398616185348129, 0.7352767332421946, 0.325699253957487, 0.05845353249038132, 0.641858521921238, 0.8871955562019045, 0.7738259734831263, 0.4950904304256668, 0.052133412962502734, 0.09235255066440262, 0.8642532345754352, 0.18756557376853278, 0.18686887960346243, 0.6876153190437099, 0.9871373882681463, 0.468621834320222, 0.2362614758308148, 0.8435009433103847, 0.3979960274398888, 0.6374335841273712, 0.9639417731770248, 0.18470452439933527, 0.8232238360615337, 0.19744621203402557, 0.35934284333462396, 0.8453275035074547, 0.6480941661827084, 0.44888309001389326, 0.06773791319043065, 0.04114657994181081, 0.14030470455672028, 0.9245235821816371]

#design variant 1
#parameters = [0.6863263950472224, 0.030471206911486526, 0.16354308637907577, 0.19079780079051356, 0.1283568092187628, 0.7534004784173401, 0.6554971373220491, 0.913431834853153, 0.7313224156019148, 0.03799793336098656, 0.11719182744183887, 0.5995899765543545, 0.7110961195259482, 0.2983737995383292, 0.7967745018402652, 0.7001714529557312, 0.8584465595199102, 0.5649029167373035, 0.5706526353107312, 0.6254003563254517, 0.19852764664883404, 0.3036132943902088, 0.22001558345911032, 0.13769642567951224, 0.07108888245824319, 0.4357522402661117, 0.6480444337066329, 0.859657913426621, 0.7358344039043376, 0.8806346268431056, 0.9614298598190284, 0.8858608794401053, 0.2663145878014823, 0.07496504721485209, 0.7236327909380954, 0.716629540626753, 0.1607419011982255, 0.2100867633720761, 0.46318526540997107, 0.3727403509592164]

#design variant 2
#parameters = [0.268949670484422, 0.6388438643632126, 0.5477613302012992, 0.885637511387602, 0.9182806559944117, 0.9085111719675296, 0.9991561738694467, 0.922424920289302, 0.821592908393413, 0.28750482600438765, 0.6103012298291838, 0.691539158536744, 0.5598189986232562, 0.1981147608570949, 0.5707026834444051, 0.647465820438139, 0.4234643182685801, 0.5346855280822317, 0.19464335871765603, 0.08809903666615193, 0.23110398327274828, 0.6962294976791072, 0.8063868934550874, 0.0618106746797924, 0.9183734927855205, 0.8518891223842804, 0.7389068565961636, 0.4245700730126485, 0.5189658701201798, 0.9201423463687924, 0.20089274178715577, 0.031164046521047983, 0.14918398996132243, 0.3987543573684912, 0.1491350530016765, 0.7467387158845056, 0.08554952590967357, 0.5027631489794012, 0.0076920079623341575, 0.6450998602986006]

#design variant 3
#parameters = [0.8971382010280249, 0.3289809698048666, 0.33532911233342555, 0.8626107715155569, 0.4912708286307663, 0.050446237159088136, 0.9902645608777924, 0.12483857854984082, 0.08370030690672958, 0.45887707557141777, 0.11649634034073575, 0.23556583584055635, 0.5088745144926603, 0.21265861534241548, 0.27284417154860074, 0.6946117454051701, 0.7150915230120592, 0.49507779364504445, 0.589745710520615, 0.07839150079231438, 0.40963335997826233, 0.343028223803282, 0.27778482200695864, 0.16311867149684223, 0.11532199706074264, 0.37601233730898187, 0.825295305352437, 0.7416310093536429, 0.9773894976715646, 0.509609003059388, 0.6005060626553582, 0.32391230403108695, 0.7583607762245201, 0.7906164459920094, 0.6291237511335771, 0.4856386223314346, 0.4536462509534053, 0.8948084439034276, 0.5143999674215958, 0.1397779505486496]

#design variant 4
#parameters = [0.2171256287047243, 0.38014488570774696, 0.814440218836235, 0.6384110225619274, 0.1860757236225622, 0.4604373775876438, 0.3387608304734736, 0.6506289579982831, 0.8316303075255694, 0.8345408960017062, 0.27437229378800854, 0.20196841927108122, 0.877315533565142, 0.4592603156776133, 0.1356376007312703, 0.8821731687756904, 0.3189503395243347, 0.43336224813015356, 0.3265373651037231, 0.3535613472161999, 0.026931322923097967, 0.4191850820746713, 0.8756989307630179, 0.14201720803843787, 0.6062776066825467, 0.7657853148992311, 0.6913501151160504, 0.8507332551756781, 0.8248152483835659, 0.961592842375467, 0.768121090336792, 0.25386519704570754, 0.2802009449160334, 0.12139708725146992, 0.3574199150851399, 0.9315892749797758, 0.3003826370991567, 0.6258951205202314, 0.9815391212643391, 0.8720457708736503]

print parameters
citygml_writer, newblist, plot_faces_list, b_attribs_list, bounding_list_list = parameterise.generate_design_variant(parameters)
citygml_writer.write(result_citygml_filepath)
#bounding list is for the generation of image for acadia paper, to show the construction of building from floor plates
#solid list shows the original position of the buildings
print newblist
display_2dlist.append(newblist)
display_2dlist.append(plot_faces_list)

time2 = time.clock() 
print "TIME TAKEN", (time2-time1)/60.0

print "VISUALISING"  
colour_list = ["WHITE", "WHITE"]
pyliburo.py3dmodel.construct.visualise(display_2dlist, colour_list)