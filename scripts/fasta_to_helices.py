#! /usr/bin/env python3
import sys
import os
import subprocess
import xlsxwriter

glut3_seq= "MGTQKVTPALIFAITVATIGSFQFGYNTGVINAPEKIIKEFINKTLTDKGNAPPSEVLLTSLWSLSVAIFSVGGMIGSFSVGLFVNRFGRRNSMLIVNLLAVTGGCFMGLCKVAKSVEMLILGRLVIGLFCGLCTGFVPMYIGEISPTALRGAFGTLNQLGIVVGILVAQIFGLEFILGSEELWPLLLGFTILPAILQSAALPFCPESPRFLLINRKEEENAKQILQRLWGTQDVSQDIQEMKDESARMSQEKQVTVLELFRVSSYRQPIIISIVLQLSQQLSGINAVFYYSTGIFKDAGVQEPIYATIGAGVVNTIFTVVSLFLVERAGRRTLHMIGLGGMAFCSTLMTVSLLLKDNYNGMSFVCIGAILVFVAFFEIGPGPIPWFIVAELFSQGPRPAAMAVAGCSNWTSNFLVGLLFPSAAHYLGAYVFIIFTGFLITFLAFTFFKVPETRGRTFEDITRAFEGQAHGADRSGKDGVMEMNSIEPAKETTTNV"
glut3_id = "P11169"

center_glut3 = [18, 67, 100, 131, 160, 194, 281, 314, 343, 376, 412, 439]
start_glut3 = [8, 56, 90, 117, 148, 184, 264, 303, 331, 361, 398, 430]
end_glut3 = [29, 79, 110, 145, 173, 204, 299, 326, 355, 391, 427, 449]

xyle_seq =  "MNTQYNSSYIFSITLVATLGGLLFGYDTAVISGTVESLNTVFVAPQNLSESAANSLLGFCVASALIGCIIGGALGGYCSNRFGRRDSLKIAAVLFFISGVGSAWPELGFTSINPDNTVPVYLAGYVPEFVIYRIIGGIGVGLASMLSPMYIAELAPAHIRGKLVSFNQFAIIFGQLLVYCVNYFIARSGDASWLNTDGWRYMFASECIPALLFLMLLYTVPESPRWLMSRGKQEQAEGILRKIMGNTLATQAVQEIKHSLDHGRKTGGRLLMFGVGVIVIGVMLSIFQQFVGINVVLYYAPEVFKTLGASTDIALLQTIIVGVINLTFTVLAIMTVDKFGRKPLQIIGALGMAIGMFSLGTAFYTQAPGIVALLSMLFYVAAFAMSWGPVCWVLLSEIFPNAIRGKALAIAVAAQWLANYFVSWTFPMMDKNSWLVAHFHNGFSYWIYGCMGVLAALFMWKFVPETKGKTLEELEALWEPETKKTQQTATL"
xyle_id = 'P0AGF4'

center_xyle = [18,65,93,139,173,208,291,325,353,383,416,452]
start_xyle = [7,50,83,126,160,198,277,311,342,370,404,443]
end_xyle = [30,81,103,152,186,219,306,339,364,397,428,462]

pfht1_seq = "MTKSSKDICSENEGKKNGKSGFFSTSFKYVLSACIASFIFGYQVSVLNTIKNFIVVEFEWCKGEKDRLNCSNNTIQSSFLLASVFIGAVLGCGFSGYLVQFGRRLSLLIIYNFFFLVSILTSITHHFHTILFARLLSGFGIGLVTVSVPMYISEMTHKDKKGAYGVMHQLFITFGIFVAVMLGLAMGEGPKADSTEPLTSFAKLWWRLMFLFPSVISLIGILALVVFFKEETPYFLFEKGRIEESKNILKKIYETDNVDEPLNAIKEAVEQNESAKKNSLSLLSALKIPSYRYVIILGCLLSGLQQFTGINVLVSNSNELYKEFLDSHLITILSVVMTAVNFLMTFPAIYIVEKLGRKTLLLWGCVGVLVAYLPTAIANEINRNSNFVKILSIVATFVMIISFAVSYGPVLWIYLHEMFPSEIKDSAASLASLVNWVCAIIVVFPSDIIIKKSPSILFIVFSVMSILTFFFIFFFIKETKGGEIGTSPYITMEERQKHMTKSVV"
pfht1_id = 'O97467'

center_pfht1 = [35,84,112,139,172,212,304,340,368,401,437,464]
start_pfht1 = [25,72,103,126,161,201,289,327,358,388,423,454]
end_pfht1 = [46,97,122,153,183,223,320,354,378,414,452,474]

stp10_seq =  "MAGGAFVSEGGGGGRSYEGGVTAFVIMTCIVAAMGGLLFGYDLGISGGVTSMEEFLTKFFPQVESQMKKAKHDTAYCKFDNQMLQLFTSSLYLAALVASFMASVITRKHGRKVSMFIGGLAFLIGALFNAFAVNVSMLIIGRLLLGVGVGFANQSTPVYLSEMAPAKIRGALNIGFQMAITIGILVANLINYGTSKMAQHGWRVSLGLAAVPAVVMVIGSFILPDTPNSMLERGKNEEAKQMLKKIRGADNVDHEFQDLIDAVEAAKKVENPWKNIMESKYRPALIFCSAIPFFQQITGINVIMFYAPVLFKTLGFGDDAALMSAVITGVVNMLSTFVSIYAVDRYGRRLLFLEGGIQMFICQLLVGSFIGARFGTSGTGTLTPATADWILAFICVYVAGFAWSWGPLGWLVPSEICPLEIRPAGQAINVSVNMFFTFLIGQFFLTMLCHMKFGLFYFFASMVAIMTVFIYFLLPETKGVPIEEMGRVWKQHWFWKKYIPEDAIIGGHDDNNTN"
stp10_id = 'Q9LT15'

center_stp10  = [37,95,120,149,180,211,296,330,360,399,431,463]
start_stp10 = [23,82,111,135,166,201,279,318,348,384,419,454]
end_stp10 =  [51,109,130,163,194,222,313,342,373,415,443,473]

glcp_seq = 'MKANKYLIFILGALGGLLYGYDNGVISGALLFIHKDIPLNSTTEGIVVSSMLIGAIVGAGSSGPLADKLGRRRLVMLIAIVFIIGALILAASTNLALLIIGRLIIGLAVGGSMSTVPVYLSEMAPTEYRGSLGSLNQLMITIGILAAYLVNYAFADIEGWRWMLGLAVVPSVILLVGIYFMPESPRWLLENRNEEAARQVMKITYDDSEIDKELKEMKEINAISESTWTVIKSPWLGRILIVGCIFAIFQQFIGINAVIFYSSSIFAKAGLGEAASILGSVGIGTINVLVTIVAIFVVDKIDRKKLLVGGNIGMIASLLIMAILIWTIGIASSAWIIIVCLSLFIVFFGISWGPVLWVMLPELFPMRARGAATGISALVLNIGTLIVSLFFPILSDALSTEWVFLIFAFIGVLAMIFVIKFLPETRGRSLEEIEYELRERTGARTE'
glcp_id = 'A0A0H2VG78'

center_glcp = [21,54,80,109,142,168,252,285,315,344,383,411]
start_glcp = [8,41,72,96,133,157,236,274,304,330,370,402]
end_glcp = [35,68,88,123,151,179,268,296,326,359,396,420]

ref_id = glut3_id
ref_seq = glut3_seq
ref_center = center_glut3
ref_start = start_glut3
ref_end = end_glut3

references = [{'id':glut3_id,'center':center_glut3, 'start':start_glut3, 'end':end_glut3},
              {'id':xyle_id,'center':center_xyle, 'start':start_xyle, 'end':end_xyle},
              {'id':pfht1_id,'center':center_pfht1, 'start':start_pfht1, 'end':end_pfht1},
              {'id':stp10_id,'center':center_stp10, 'start':start_stp10, 'end':end_stp10},
              {'id':glcp_id, 'center': center_glcp, 'start':start_glcp, 'end':end_glcp}]

def main():

    in_fasta = sys.argv[1] # list of curated sequences in one fasta file
    dir = sys.argv[2] # directory in which to store result files
    pw_ali_folder = sys.argv[3] # folder with pairwise alignments from either hhblits or TM-align
    tm_align = sys.argv[4] # if 1 then it's alignments from TM-align, if 0 alignments from hhblits
    # if tm-align is 1, expect another argument with parsed alignments
    pw_ali_folder_af = sys.argv[5]
    final = dir
    dir += 'dgpred_results/'

    # if not os.path.exists(dir):
    #     os.mkdir(dir)

    center_found = 0
    next_to_it = 0
    center_via_start_end = 0
    center_via_start  = 0
    center_via_end = 0
    total = 0
    # read in sequences in fasta format
    seqs, names, species = read_fasta(in_fasta)
    energies = []

    # clean names and align each sequence with reference
    for i in range(0, len(seqs)):
        seq = ''.join(seqs[i])
        # set reference with the highest alignment score
        set_reference(pw_ali_folder, names[i], tm_align)
        #  infer helix positions based on reference
        if tm_align == "1":
            coords_seq, coords_ref = get_coords_hhblits(pw_ali_folder_af, names[i])
        else:
            coords_seq, coords_ref = get_coords_hhblits(pw_ali_folder + 'hhalign_', names[i])
        center_seq_list, start_seq_list, end_seq_list, center_found, next_to_it, center_via_start_end, center_via_start, center_via_end, total = get_seq_coords_hhblits(seq, names[i], coords_seq, coords_ref, center_found, next_to_it, center_via_start_end, center_via_start, center_via_end, total)
        adjusted_center_seq_list = check_minimum_neighours(seq, names[i], center_seq_list, start_seq_list, end_seq_list)
        # print(names[i], ',', adjusted_center_seq_list[6] + 10)
        TM_new_full, TM_new_19 = get_helices_hhblits(seq, names[i], adjusted_center_seq_list, start_seq_list, end_seq_list, dir)
        # calculate insertion energies for inferred helices
        dgpred(dir, names[i], 'full')
        dgpred(dir, names[i], '19')
        energy_full, helices_full = parse_results(dir, names[i], 'full')
        energy_19, helices_19 = parse_results(dir, names[i], '19')
        helix_info = {"id":names[i], "species":species[i], "ref_seq":ref_id, "energies_full":energy_full, "energies_19":energy_19, "helices_full": helices_full, "helices_19":helices_19}
        energies.append(helix_info)

    output_results(in_fasta, final, energies)
    print("found: ", center_found)
    print("total: ", total)
    print("next to it : ", next_to_it)
    print("start and end: ", center_via_start_end)
    print("start only : ", center_via_start)
    print("end only : ", center_via_end)

def check_minimum_neighours(seq, id, center_seq_list, start_seq_list, end_seq_list):

    coords_range = 3 # refinement range
    adjusted_center_seq_list = []
    for i in range(0,len(center_seq_list)):
        # first find all possible positions and obtain energy
        energy_list   = []
        if center_seq_list[i] > -1:
            center = center_seq_list[i]
            if i > 0:
                end_left = end_seq_list[i - 1]
                missing_helix = 2
                while (end_left  ==  -1) and (i - missing_helix > -1):
                    end_left = end_seq_list[i - missing_helix]
            # first helix -> 0
            else:
                end_left = -1
            if i < len(center_seq_list) - 1:
                start_right = start_seq_list[i + 1]
                missing_helix = 2
                while ((start_right  ==  -1) and (i + missing_helix < len(start_seq_list))):
                    start_right = start_seq_list[i + missing_helix]
            # last helix -> len(seq)
            else:
                start_right = len(seq) - 2
            j = -1 * coords_range
            while j <= coords_range:
                new_center = center + j
                new_start = new_center - 9
                new_end = new_center + 10
                # make sure it's not spilling over into neighbouring helices
                # also make sure it's not spilling over the ends of the sequence
                if end_left == -1:
                    end_left = 0
                if start_right == -1:
                    start_right = len(seq)
                if new_start > end_left and new_end < start_right:
                    energy = dgpred_single(seq[new_start:new_end])
                    energy_list.append({'energy':energy, 'start':new_start, 'end':new_end, 'center': new_center})
                j += 1
        else:
            adjusted_center_seq_list.append(-1)

        # then find minimum and redefine center position
        if len(energy_list) > 0:
            min_energy = energy_list[0]
            for helix in energy_list:
                if min_energy['energy'] > helix['energy']:
                    min_energy = helix
            adjusted_center_seq_list.append(min_energy['center'])
        else:
            print('adjustment not possible: ', id)
            print(end_left, center, start_right)
            adjusted_center_seq_list.append(center_seq_list[i])

    if len(adjusted_center_seq_list) != 12:
        print('WARNING')

    return adjusted_center_seq_list


def set_reference(dir, id, tm_align):

    global ref_id
    global ref_seq
    global ref_center
    global ref_start
    global ref_end

    max_score = 0.0
    max_ref = ''

    for ref in references:
        if ref['id'] != id:
            if tm_align == "1":
                # check original tm align result file for score
                ali = dir + ref['id'] + '/' + id + '.a3m_ali.txt'
                counter = 0

                with open(ali) as input:
                    for line in input:
                        line = line.strip()
                        if 'TM-score=' in line:
                            ali_score = line.split('= ')[1].split(' ')[0]
                            if float(ali_score) > max_score:
                                max_score = float(ali_score)
                                max_ref = ref['id']
                                max_center  = ref['center']
                                max_start = ref['start']
                                max_end = ref['end']
            else:
                # check hhblits alignments for reference sequence with highest score
                ali =  dir + 'hhalign_' + ref['id'] + '/' + id + '.hhr'
                counter = 0

                with open(ali) as input:
                    for line in input:
                        line = line.strip()
                        counter += 1
                        if counter == 10:
                            ali_score = line.split()[5]
                            if float(ali_score) > max_score:
                                max_score = float(ali_score)
                                max_ref = ref['id']
                                max_center  = ref['center']
                                max_start = ref['start']
                                max_end = ref['end']

    ref_id = max_ref
    ref_center =  [i - 1 for i in max_center]
    ref_start = [i - 1 for i in max_start]
    ref_end = [i - 1 for i in max_end]

    return ref_id, ref_center, ref_start, ref_end


def get_helices_hhblits(seq, id, center_seq_list, starts, ends, dir):

    TM_full = []
    TM_19 = []

    TM_full_file = open(dir + id + '_TM_full.txt', "w")
    TM_19_file = open(dir + id + '_TM_19.txt', "w")

    for center in center_seq_list:
        if center > -1:
            start_19 =  center - 9
            end_19 = center + 10
            while start_19 < 0:
                start_19 += 1
            while end_19 >= len(seq):
                end_19 -= 1
            if len(seq[start_19:end_19])  >  0:
                TM_19.append(seq[start_19:end_19])
                TM_19_file.write(seq[start_19:end_19] + "\n")
            else:
                TM_19.append('NULL')
                TM_19_file.write("N\n")
        else:
            TM_19.append('NULL')
            TM_19_file.write("N\n")

    for i in range(0,len(starts)):
        if starts[i] > -1 and ends[i] > -1:
            while ends[i] > len(seq):
                ends[i] -= 1
            TM_full.append(seq[starts[i]:ends[i]])
            TM_full_file.write(seq[starts[i]:ends[i]] + "\n")
        else:
            TM_full.append('NULL')
            TM_full_file.write("N\n")

    TM_full_file.close()
    TM_19_file.close()

    return TM_full, TM_19

def get_seq_coords_hhblits(seq, id, coords_seq, coords_ref, center_found, next_to_it, center_via_start_end, center_via_start, center_via_end, total):

    center_seq_list = []
    start_seq_list = []
    end_seq_list = []

    for center in ref_center:
        found = 0
        total += 1
        for i in range(0,len(coords_ref)):
            if coords_ref[i] == center:
                found = 1
                center_found += 1
                center_seq = coords_seq[i]
                center_seq_list.append(center_seq)
        if found == 0:
            # check to left and right
            print('not found! ', id)
            pos_seq = check_neighbours(center, coords_seq,  coords_ref)
            if pos_seq > -1:
                next_to_it += 1
            center_seq_list.append(pos_seq)

    for start in ref_start:
        found = 0
        for i in range(0,len(coords_ref)):
            if coords_ref[i] == start:
                found = 1
                start_seq = coords_seq[i]
                start_seq_list.append(start_seq)
        if found == 0:
            # check to left and right
            pos_seq = check_neighbours(start, coords_seq,  coords_ref)
            start_seq_list.append(pos_seq)

    for end in ref_end:
        found = 0
        for i in range(0,len(coords_ref)):
            if coords_ref[i] == end:
                found = 1
                end_seq = coords_seq[i]
                end_seq_list.append(end_seq)
        if found == 0:
            # check to left and right
            pos_seq = check_neighbours(end, coords_seq,  coords_ref)
            end_seq_list.append(pos_seq)

    # infer positions that did not align from positions of the helix that did
    for j in range(0, len(center_seq_list)):
        if center_seq_list[j] == -1:
            if start_seq_list[j] > -1 and end_seq_list[j] > -1:
                if ((start_seq_list[j] + end_seq_list[j]) / 2)  > -1 and ((start_seq_list[j] + end_seq_list[j]) / 2) < len(seq):
                    center_seq_list[j] = (start_seq_list[j] + end_seq_list[j]) / 2
                    center_via_start_end += 1
            elif start_seq_list[j] > -1:
                if start_seq_list[j] + 9 < len(seq):
                    center_seq_list[j] = start_seq_list[j] + 9
                    center_via_start += 1
            elif end_seq_list[j] > -1:
                if end_seq_list[j] - 10 > -1:
                    center_seq_list[j] = end_seq_list[j] - 10
                    center_via_end += 1
        if start_seq_list[j] == -1:
            if center_seq_list[j] > -1:
                if center_seq_list[j] - 9 > -1:
                    start_seq_list[j] = center_seq_list[j] - 9
        if end_seq_list[j] == -1:
            if center_seq_list[j] > -1:
                if center_seq_list[j] + 10 < len(seq):
                    end_seq_list[j] = center_seq_list[j] + 10

    return center_seq_list, start_seq_list, end_seq_list, center_found, next_to_it, center_via_start_end, center_via_start, center_via_end, total

def check_neighbours(pos, coords_seq,  coords_ref):

    for i in range(0,len(coords_ref)):
        if coords_ref[i] == (pos - 1):
            pos_seq = coords_seq[i]
            return pos_seq

    for i in range(0,len(coords_ref)):
        if coords_ref[i] == (pos + 1):
            pos_seq = coords_seq[i]
            return pos_seq

    return -1

def get_coords_hhblits(dir, id):

    infile = dir + ref_id + '/' + id + '.atab'
    counter = 1
    coords_seq_list = []
    coords_ref_list = []
    with open(infile) as input:
        for line in input:
            line = line.strip()
            if len(line) == 0:
                continue
            else:
                if counter < 4:
                    counter += 1
                else:
                    coords_seq = line.split()[0]
                    coords_ref = line.split()[1]
                    #adjust start counting at 0
                    coords_seq_list.append(int(coords_seq) - 1)
                    coords_ref_list.append(int(coords_ref) - 1)

    return coords_seq_list, coords_ref_list


def output_results(in_fasta, dest, energies):

    output = dest + in_fasta.split('/')[-1].split(".")[0] + "_helices" ".xlsx"

    workbook = xlsxwriter.Workbook(output)
    cell_format = workbook.add_format({'bold': True})
    cell_format_clr = workbook.add_format({'bold': True, 'fg_color': '#D7E4BC'})

    worksheet1 = workbook.add_worksheet("INSERTION_ENERGIES_FULL")
    worksheet2 = workbook.add_worksheet("INSERTION_ENERGIES_19")
    worksheet3 = workbook.add_worksheet("INPUT_STRING_FULL")
    worksheet4 = workbook.add_worksheet("INPUT_STRINGS_19")

    worksheet1.set_column('A:A', 15)
    worksheet2.set_column('A:A', 15)
    worksheet3.set_column('A:A', 15)
    worksheet4.set_column('A:A', 15)

    worksheet1.write('A1', 'Uniprot ID', cell_format_clr)
    worksheet2.write('A1', 'Uniprot ID', cell_format_clr)
    worksheet3.write('A1', 'Uniprot ID', cell_format_clr)
    worksheet4.write('A1', 'Uniprot ID', cell_format_clr)
    worksheet1.write('B1', 'Species', cell_format_clr)
    worksheet2.write('B1', 'Species', cell_format_clr)
    worksheet3.write('B1', 'Species', cell_format_clr)
    worksheet4.write('B1', 'Species', cell_format_clr)
    worksheet1.write('C1', 'Reference sequence', cell_format_clr)
    worksheet2.write('C1', 'Reference sequence', cell_format_clr)
    worksheet3.write('C1', 'Reference sequence', cell_format_clr)
    worksheet4.write('C1', 'Reference sequence', cell_format_clr)


    for i in range(1,13):
        worksheet1.set_column(chr(97+i + 2).upper()+":"+chr(97+i).upper(), 12)
        worksheet1.write(chr(97+i + 2).upper() + str(1), 'TM' + str(i) + '_energy', cell_format_clr)
        worksheet2.set_column(chr(97+i + 2).upper()+":"+chr(97+i).upper(), 12)
        worksheet2.write(chr(97+i + 2).upper() + str(1), 'TM' + str(i) + '_energy', cell_format_clr)
    for i in range(1,13):
        worksheet3.set_column(chr(97+i + 2).upper()+":"+chr(97+i).upper(), 25)
        worksheet3.write(chr(97+i + 2).upper() + str(1), 'TM' + str(i), cell_format_clr)
        worksheet4.set_column(chr(97+i + 2).upper()+":"+chr(97+i).upper(), 25)
        worksheet4.write(chr(97+i + 2).upper() + str(1), 'TM' + str(i), cell_format_clr)

    # parse data
    ids = []
    energies_19 = []
    energies_full = []
    helix_full = []

    counter = 1
    for tm_set in energies:
        counter += 1
        worksheet1.write('A' + str(counter), tm_set["id"])
        worksheet2.write('A' + str(counter), tm_set["id"])
        worksheet3.write('A' + str(counter), tm_set["id"])
        worksheet4.write('A' + str(counter), tm_set["id"])
        worksheet1.write('B' + str(counter), tm_set["species"])
        worksheet2.write('B' + str(counter), tm_set["species"])
        worksheet3.write('B' + str(counter), tm_set["species"])
        worksheet4.write('B' + str(counter), tm_set["species"])
        worksheet1.write('C' + str(counter), tm_set["ref_seq"])
        worksheet2.write('C' + str(counter), tm_set["ref_seq"])
        worksheet3.write('C' + str(counter), tm_set["ref_seq"])
        worksheet4.write('C' + str(counter), tm_set["ref_seq"])
        worksheet1.write_row('D' + str(counter) + ":", tm_set["energies_full"])
        worksheet2.write_row('D' + str(counter) + ":", tm_set["energies_19"])
        worksheet3.write_row('D' + str(counter) + ":", tm_set["helices_full"])
        worksheet4.write_row('D' + str(counter) + ":", tm_set["helices_19"])

    workbook.close()

def parse_results(dir, id, version):

    input = dir + id + "_TM_" + version + ".html"
    result_file = open(input, "r").read()

    energies = []
    helices = []

    begin = result_file.find("Predicted")
    last_begin = result_file.find("<tr><td>", begin + 1)
    last_stop = result_file.find("</td></tr>", last_begin + 1)
    last_begin = result_file.find("<tr><td>", last_begin + 1)
    counter = 0
    while (last_begin > 0):
        counter += 1
        last_stop = result_file.find("</td></tr>", last_stop + 1)
        last_seq_end = result_file.find("</td><td>&nbsp;", last_begin, last_stop)
        last_energy_start = result_file.find(";</td><td>", last_begin, last_stop)
        last_energy_stop = result_file.find("</td><td><a", last_energy_start, last_stop)
        helix = result_file[last_begin:last_seq_end].split("<td>")[-1]
        energy = result_file[last_energy_start:last_energy_stop].split("<td>")[-1]

        if len(energy) > 0:
            floaty_energy = float(energy)
        else:
            floaty_energy = energy

        energies.append(floaty_energy)
        helices.append(helix)

        last_begin = result_file.find("<tr><td>", last_stop + 1)

    return energies, helices

def dgpred_single(helix):

    dgpred_exe = "/Users/charlotte/Programs/dgpred/analyze.pl"

    process = subprocess.Popen([dgpred_exe, helix],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    inter = str(stdout).split("length")[2]
    if '+-0.00' in inter:
        energy = 0.00
    elif '+--0.00' in inter:
        energy = 0.00
    else:
        energy = float(str(stdout).split("length")[2].split("span")[2].split("<")[0].split(">")[1])

    return energy

def dgpred(dest, id, version):

    dgpred_exe = "/Users/charlotte/Programs/dgpred/calc_dG.pl"
    i = 0
    input = dest + id + "_TM_" + version + ".txt"
    output = dest + id + "_TM_" + version + ".html"

    process = subprocess.Popen([dgpred_exe, input, '-o', output],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()


def read_fasta(infile):

    nams = []
    seqs = []
    species = []
    nam = ""
    seq = ""
    spec = ""
    with open(infile) as input:
        for line in input:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == ">":
                seqs.append([s.upper() for s in seq])
                nams.append(nam)
                species.append(spec)
                seq = []
                nam = line.replace(">", "").split()[0].split("|")[1]
                spec = line.replace(">", "").split()[0].split("|")[2]
            else:
                if len(nams) == 0:
                    print("error")
                    exit()
                seq += list(line)
    seqs.append([s.upper() for s in seq])
    nams.append(nam)
    species.append(spec)

    return (seqs[1:], nams[1:], species[1:])

if __name__ == "__main__":
    main()
