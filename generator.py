from PIL import Image
# additionally, text overlay is needed. Import the ImageDraw and ImageFont modules
from PIL import ImageDraw
from PIL import ImageFont

import os


code_of_conduct_HKIE_type = {
    # Profession, Colleagues, Employers/Clients, Public
    "1": "Profession",
    "2": "Colleagues",
    "3": "Employers/Clients",
    "4": "Public"
}


def get_code_of_conduct_HKIE_type(rule):
    # for rule 4, if it has not any ., then it is "Public - Environment", otherwise, it is "Public"
    if rule[0] == "4":
        return "Public (particulars)" if not "." in rule else "Public"
    return code_of_conduct_HKIE_type[rule[0]]


code_of_conduct_HKIE = {
    # unchanged
    # "1.0": ["123456789012345678901234567890123456789012345", "123456789012345678901234567890123456789012345"],
    # unchanged
    "1.1": ["Discharge all responsibilities with          ", "integrity, dignity, fairness, & courtesy     "],
    # unchanged
    "1.2": ["No self-laudatory advertising                ", "nor improperly solicit work                  "],
    "1.3": ["Provide objective, reliable & honest         ", "opinions to the best of ones ability         "],
    "1.4": ["Avoid environmental damage                   ", "and waste of natural resources               "],
    # unchanged
    "1.5": ["Ensure adequate development                  ", "of ones professional competence              "],
    "1.6": ["Accept responsibility for actions,           ", "ensuring delegated authority competent       "],
    # unchanged
    "1.7": ["Never undertake responsibilities             ", "for which one is unqualified to work on      "],
    "1.8": ["Treat colleagues fairly                      ", "Never misuse position                        "],
    "1.9": ["Follow local standards abroad                ", "Fall back to HKIE code if unavailable        "],
    # unchanged
    "1.10": ["When working in other fields                ", "pay attention & respect their ethics         "],

    "2.1": ["Seek and offer honest criticism              ", "Properly credit contributions                "],
    "2.2": ["Exchange information & experience            ", "with other engineers                         "],
    # unchanged
    "2.3": ["Support colleagues and trainees              ", "in their professional development            "],
    "2.4": ["Never abuse HKIE connections                 ", "for business interests                       "],
    "2.5": ["Report unethical practice to HKIE            ", "w/o falsely injuring reputation              "],
    # unchanged
    "2.6": ["Support the aims of HKIE                     ", "and its activities                           "],

    "3.1": ["Offer complete loyalty and fairness          ", "to employers/clients, past&present           "],
    "3.2": ["Avoid conflicts of interest                  ", "Disclose any possible conflicts              "],
    "3.3": ["Never accept financial/contractural          ", "obligations w/o authorization                "],
    "3.4": ["Advise on consequences of                    ", "overruling engineering judgment              "],
    # unchanged
    "3.5": ["Advise on consequences of                    ", "any relevant developments                    "],
    "3.6": ["Never accept gifts or entertainment          ", "from business partners w/o consent           "],
    "3.7": ["Co-operate with experts                      ", "whenever necessary                           "],
    # unchanged
    "3.8": ["Safeguard confidential info                  ", "despite offers of personal gains             "],

    "4.1": ["Protect safety, health,                      ", "and welfare of public                        "],
    "4.2": ["Disclose associations                        ", "when making public statements                "],
    "4.3": ["Promote public understanding                 ", "of the engineering profession                "],
    "4.4": ["Assess environmental consequences            ", "Strive to prevent or minimize damage         "],

    "4a":  ["Create a healthy and agreeable               ", "environment (outdoors & indoors)             "],
    "4b":  ["Minimize non-renewable resource use          ", "Conserve energy & avoid waste                "],
    "4c":  ["Consider consequences of proposal            ", "in public health and local customs           "],
    "4d":  ["Assess environmental impacts                 ", "Select sustainable options                   "],
    "4e":  ["In proposals, consider & explain             ", "measures helping the environment             "],
    "4f":  ["Promote ecosystem interdependence            ", "and sustainable development                  "],
    "4g":  ["Balance costs with best benefit to           ", "the environment and human society            "],
    "4h":  ["Get management follow environmental policies ", "as stating intent =/= legislative compliance "]
}

code_of_conduct_HKIE_humanwords = {
    "1.0": "1234567890123456789012345678901234567890123",
    "1.1": "be honest & respectful    ",
    "1.2": "never brag nor try to get work unfairly    ",
    "1.3": "give honest & informed opinions          ",
    "1.4": "i.e. environmental protection     ",
    "1.5": "keep skills up to date                ",
    "1.6": "be responsible, delegate tasks wisely ",
    "1.7": "don't do work outside of abilities     ",
    "1.8": "don't abuse power ",
    "1.9": "local rules first, fallback to HKIE",
    "1.10": "respect other professions    ",

    "2.1": "constructive feedback, credit other's work",
    "2.2": "share knowledge & experience",
    "2.3": "help colleagues & trainees develop skills  ",
    "2.4": "don't use connections for personal gain",
    "2.5": "report unethical behavior carefully        ",
    "2.6": "support HKIE goals and activities          ",

    "3.1": "be loyal and fair to employer / client",
    "3.2": "e.g. never accept money from competitors",
    "3.3": "cannot make binding agreements",
    "3.4": "warn consequences if judgment overruled    ",
    "3.5": "keep employer informed on the news         ",
    "3.6": "don't accept bribes",
    "3.7": "collaborate w/ experts when necessary",
    "3.8": "keep confidentiality",

    "4.1": "it is the 'overriding interest'            ",
    "4.2": "e.g. declare sponsorships                  ",
    "4.3": "introduce public & children to engineering ",
    "4.4": "environmental protection is a priority",
    "4a": "e.g. minimize pollution & noise             ",
    "4b": "save the Earth",
    "4c": "more holistic approach to proposals",
    "4d": "choose the 'green' option",
    "4e": "explain environmental protection measures",
    "4f": "promote sustainable development",
    "4g": "balance costs with environmental benefits",
    "4h": "talk is cheap, action matters"
}

code_of_conduct_WFEO_type = {
    "1": "Integrity",
    "2": "Competence",
    "3": "Leadership",
    "4": "Environmental Protection"
}

"""
1. DEMONSTRATE INTEGRITY 

1.1 Refrain from fraudulent, corrupt or criminal practices 
1.2 Be objective and truthful 
1.3 Practise fairly and with good faith towards clients, colleagues and others 


2. PRACTISE COMPETENTLY 

2.1 Practise in a careful and diligent manner in accordance with their areas of competence 
2.2 Practise in accordance with accepted engineering practices, standards and codes 
2.3 Maintain and strive to enhance the body of knowledge in which they practise 


3. EXERCISE LEADERSHIP 

3.1 Practise so as to enhance the quality of life in society 
3.2 Strive to contribute to the advancement of the body of knowledge within which they practise, and to the profession in general 
3.3 Foster the public’s understanding of technical issues and the role of engineering 


4. PROTECT THE NATURAL AND BUILT ENVIRONMENT 

4.1 Create and implement engineering solutions for a sustainable future 
4.2 Be mindful of the economic, societal and environmental consequences of actions or projects 
4.3 Promote and protect the health, safety and well-being of the community and the environment

"""

code_of_conduct_WFEO = {
    "1.1": ["Refrain from fraudulent, corrupt ", "or criminal practices"],
    "1.2": ["Be objective ", "and truthful"],
    "1.3": ["Practise fairly and with good faith ", "towards clients, colleagues and others"],
    "2.1": ["Practise in a careful and diligent manner", "in accordance with their areas of competence"],
    "2.2": ["Practise in accordance with accepted ", "engineering practices, standards and codes"],
    "2.3": ["Maintain and strive to enhance the ", "body of knowledge in which they practise"],
    "3.1": ["Practise so as to enhance the ", "quality of life in society"],
    "3.2": ["Contribute to advancement of knowledge", "in their profession and in general"],
    "3.3": ["Foster the public’s understanding of ", "technical issues and the role of engineering"],
    "4.1": ["Create and implement engineering solutions", "for a sustainable future"],
    "4.2": ["Be mindful of the economic, societal and ", "environmental consequences"],
    "4.3": ["Promote and protect the health, safety and ", "well-being of the community and environment"]
}

code_of_conduct_WFEO_humanwords = {
    "1.1": "no cheating",
    "1.2": "be honest",
    "1.3": "be fair",
    "2.1": "be careful",
    "2.2": "follow the rules",
    "2.3": "keep learning",
    "3.1": "improve society",
    "3.2": "improve the profession",
    "3.3": "educate the public",
    "4.1": "save the world",
    "4.2": "think before you act",
    "4.3": "keep people safe"
}

"""
AIAA Code of Ethics

**1: General Ethical Expectations**

A. Hold paramount the safety, health, and welfare of the public

**2: Professional Integrity**


B. Avoid real and perceived conflicts of interest
C. Act as an honest and fair agent in all professional interactions
D. Reject bribery, fraud, and corruption in all their forms and avoid unlawful conduct in professional activities
E. Properly credit the contributions of others, accept and offer honest and constructive criticism of technical work, and acknowledge and correct errors promptly
F. Issue statements or present information in an objective and truthful manner, based on available data
G. Undertake only those tasks for which one is qualified by training or experience, or for which one can reasonably become qualified with proper preparation, education, and training

**3: Personal Conduct**

H. Treat all persons with respect, fairness, and dignity, and never engage in any form of harassment or discrimination
I. Avoid harming others, their property, their reputations, or their employment through false or malicious statements or through unlawful or otherwise wrongful actions

"""

code_of_conduct_AIAA = {
    "1.A": ["Hold paramount the safety, health,", "and welfare of the public"],
    "2.B": ["Avoid real and perceived", "conflicts of interest"],
    "2.C": ["Act as an honest and fair agent", "in all professional interactions"],
    "2.D": ["Reject bribery, fraud, and corruption", "Avoid unlawful conduct in the profession"],
    "2.E": ["Properly credit contributions, accept&offer", "constructive criticism, correct errors ASAP"],
    "2.F": ["Issue statements / present information in", "objective and truthful manner"],
    "2.G": ["Undertake only tasks for which one is", "qualified by training or experience"],
    "3.H": ["Treat all with respect, fairness, & dignity", "Never engage in harassment or discrimination"],
    "3.I": ["Avoid harming others (property&reputations)", "or their employment through wrongful actions"]
}

code_of_conduct_AIAA_humanwords = {
    "1.A": "keep people safe",
    "2.B": "no conflicts of interest",
    "2.C": "be honest and fair",
    "2.D": "no bribes, fraud, or corruption",
    "2.E": "give credit, improve w/ criticism",
    "2.F": "be truthful",
    "2.G": "only do what you're qualified for",
    "3.H": "be respectful, fair, and dignified",
    "3.I": "don't harm others"
}

code_of_conduct_AIAA_type = {
    "1": "General",
    "2": "Integrity",
    "3": "Conduct"
}


def generate_rule_image(rule="1.1", ruletype="HKIE", rescale=3, width_multiple=5, header="Rule 1.1", description=["multiple", "lines"], human_words=[], rescale2=2, output_path="output/rule1.1-text.png"):
    # open up rule1.png, for example, since it is rule 1.1, so we take the first 1
    rule_number = rule[0]
    imgfilename = f"{ruletype}rule{rule_number}.png"
    

    BORDER_WIDTH = 3

    image_original = Image.open(imgfilename)
    
    # simply open imgfilename and rescale 10x larger using nearest neighbor and save to icons folder
    # ensure icons folder exists
    os.makedirs("icons", exist_ok=True)
    image_original.resize(
        (image_original.width * 10, image_original.height * 10),
        Image.NEAREST
    ).save(os.path.join("icons", imgfilename.replace(".png", "_10x.png"))   )


    # rescale the image 4 times larger using nearest neighbor
    image = image_original.resize(
        (int(image_original.width * rescale),
         int(image_original.height * rescale)),
        Image.NEAREST
    )

    # pad the image to the right with black until the width becomes width times width_multiple
    width, height = image.size
    new_width = int(width * width_multiple)
    new_image = Image.new("RGB", (new_width, height), color="black")
    new_image.paste(image, (2*rescale, 0))

    draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype(
        "MxPlus_ToshibaSat_8x16.ttf", size=16
    )

    # get the colors in image and there should be only 2 colors. Get the non-black one and paint a BORDER_WIDTH-pixel wide border around new_image
    colors = list(set(new_image.getdata()))
    colors.remove((0, 0, 0))
    color = colors[0]
    draw.rectangle([0, 0, new_width-BORDER_WIDTH//2, height -
                   BORDER_WIDTH//2], outline=color, width=BORDER_WIDTH)

    # also draw a vertical line just after the original image
    draw.line([width+4*rescale-BORDER_WIDTH//2-1, 0, width+4*rescale -
              BORDER_WIDTH//2-1, height], fill=color, width=BORDER_WIDTH)

    # draw header
    draw.text((width + 8+6+4, 6+4), header, font=font, fill="white")

    # draw description
    for i, line in enumerate(description):
        # warn if line is too long, threshold 44
        if len(line.strip()) > 44:
            print(
                f"Warning: line {i+1} of description is too long, it has {len(line)} characters.")
            print(f"Line {i+1}: {line}")
        draw.text((width + 8+6+4, 6+4+1 + 16 + 6 + i * 16),
                  line, font=font, fill="white")

    # draw human words
    if human_words:
        for i, line in enumerate(human_words):
            # warn if line is too long, threshold 44
            if len(line.strip()) > 44:
                print(
                    f"Warning: line {i+1} of description is too long, it has {len(line)} characters.")
                print(f"Line {i+1}: {line}")
            draw.text((width + 8+6+4, 6+4+2 + 16 + 6 + len(description) *
                      16 + 6 + i * 16), line, font=font, fill="white")

    # open font MxPlus_HP_100LX_6x8.ttf as font2

    font2 = ImageFont.truetype(
        # "MxPlus_HP_100LX_6x8.ttf", size=8
        "Mx437_EverexME_5x8.ttf", size=8
    )

    # rescale new_image 2x larger using nearest neighbor
    new_image = new_image.resize(
        (new_image.width * 2, new_image.height * 2),
        Image.NEAREST
    )

    # draw text vertically "Copyright"
    text_copyright = "(c) Evan @ ico-lang2030.evnchn.io"
    # first get the width and height of the text
    text_width, text_height = font2.getlength(text_copyright), 8

    # round up text_width and text_height to the nearest integer

    text_width, text_height = int(text_width), int(text_height)
    # make a new image with the text
    text_image = Image.new("RGB", (text_width, text_height), color="black")
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text((0, 0), text_copyright, font=font2, fill="white")

    # rotate the text_image 90 degrees anti-clockwise then paste it to the bottom right corner of new_image

    # y used to be new_image.height - text_width - BORDER_WIDTH*2
    text_image = text_image.rotate(90, expand=True)
    new_image.paste(text_image, (new_image.width - text_height -
                    BORDER_WIDTH*2, new_image.height//2 - text_width // 2))

    # rescale new_image to rescale2 times larger using nearest neighbor
    new_image = new_image.resize(
        (new_image.width * rescale2, new_image.height * rescale2),
        Image.NEAREST
    )

    # ensure the output folder exists

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # save to output.png for now
    new_image.save(output_path)
    
    
    


def generate_rule_image_HKIE(rule, output_path="output/rule1.1-text.png"):
    generate_rule_image(rule=rule, ruletype="HKIE", header=f"HKIE Rule H{rule} - {get_code_of_conduct_HKIE_type(rule)}", description=code_of_conduct_HKIE[rule], human_words=[
                        "("+code_of_conduct_HKIE_humanwords[rule].strip()+")"], output_path=output_path)


# generate all the rules
for rule in code_of_conduct_HKIE.keys():
    generate_rule_image_HKIE(rule, output_path=f"output/HKIE_rule{rule}.png")

for rule in code_of_conduct_WFEO.keys():
    generate_rule_image(rule=rule, ruletype="WFEO", header=f"WFEO Rule W{rule} - {code_of_conduct_WFEO_type[rule[0]]}", description=code_of_conduct_WFEO[rule], human_words=[
                        "("+code_of_conduct_WFEO_humanwords[rule].strip()+")"], output_path=f"output/WFEO_rule{rule}.png")

for rule in code_of_conduct_AIAA.keys():
    generate_rule_image(rule=rule, ruletype="AIAA", header=f"AIAA Rule A{rule} - {code_of_conduct_AIAA_type[rule[0]]}", description=code_of_conduct_AIAA[rule], human_words=[
                        "("+code_of_conduct_AIAA_humanwords[rule].strip()+")"], output_path=f"output/AIAA_rule{rule}.png")
    
# for each image opened in generate_rule_image, list it in a list


# read output/HKIE_rule1.1.png and create an empty and transparent image with the same size, save it as "empty.png" in asset folder

read_image = Image.open("output/HKIE_rule1.1.png")
empty_image = Image.new("RGBA", read_image.size, (0, 0, 0, 0))
#ensure asset folder exists
os.makedirs("assets", exist_ok=True)
empty_image.save("assets/empty.png")