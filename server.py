import nicegui
from nicegui import ui, app

"""
HKIE markdown string section
"""

HKIE_markdown = """
# Rule 1: Responsibility to the Profession

A member of the Institution shall order his conduct so as to uphold the dignity, standing and reputation of the profession.

In pursuance of this rule a member shall, inter alia:

* 1.1. discharge his professional responsibilities with integrity, dignity, fairness and courtesy;
* 1.2. not allow himself to be advertised in self-laudatory language nor in any manner derogatory to the dignity of his profession, nor improperly solicit professional work for himself or others;
* 1.3. give opinions in his professional capacity that are, to the best of his ability, objective, reliable and honest;
* 1.4. take reasonable steps to avoid damage to the environment and the waste of natural resources or the products of human skill and industry;
* 1.5. ensure adequate development of his professional competence;
* 1.6. accept responsibility for his actions and ensure that persons to whom he delegates authority are sufficiently competent to carry out the associated responsibility;
* 1.7. not undertake responsibility which he himself is not qualified and competent to discharge;
* 1.8. treat colleagues and co-workers fairly and not misuse the advantage of position;
* 1.9. when working in a country other than Hong Kong, order his conduct according to the existing recognised standards of conduct in that country, except that he should abide by these rules as applicable in the absence of local standards;
* 1.10. when working within the field of another profession, pay due attention to the ethics of that profession.

---===---

# Rule 2: Responsibility to Colleagues

A member of the Institution shall not maliciously or recklessly injure nor attempt to injure whether directly or indirectly the professional reputation of another engineer, and shall foster the mutual advancement of the profession.

In pursuance of this rule a member shall, inter alia:

* 2.1. where appropriate, seek, accept and offer honest criticism of work and properly credit the contributions of others;
* 2.2. seek to further the interchange of information and experience with other engineers;
* 2.3. assist and support colleagues and engineering trainees in their professional development;
* 2.4. not abuse his connection with the Institution to further his business interests;
* 2.5. not maliciously or falsely injure the professional reputation, prospects or practice of another member; provided however that he shall bring to the notice of the Institution any evidence of unethical, illegal or unfair professional practice;
* 2.6. support the aims and activities of the Institution.

---===---

# Rule 3: Responsibility to Employers or Clients

A member of the Institution shall discharge his duties to his employer or client with integrity and in accordance with the highest standards of business ethics.

In pursuance of this rule a member shall, inter alia:

* 3.1. offer complete loyalty to his employer or client, past and present, in all matters concerning remuneration and in all business affairs and at the same time act with fairness between his employer or client and any other party concerned;
* 3.2. avoid engaging in business, investments or activities which conflict with the interests of his employer or client, and inform his employer or client in writing of any possible conflict between his own financial interests, or those of his immediate family, and the interests of his client or employer;
* 3.3. not accept any financial or contractual obligation on behalf of his employer or client without their authority;
* 3.4. where possible, advise those concerned of the consequences to be expected if his engineering judgment, in areas of his responsibility, is overruled by a non-technical authority;
* 3.5. advise his employer or client in anticipating the possible consequences of relevant developments that come to his knowledge;
* 3.6. neither give nor accept any gift, entertainment, payment or service of more than nominal value, to or from those having a business relationship with his employer or client without the consent of the latter;
* 3.7. where necessary, co-operate with or arrange for the services of other experts wherever an employer's or client's interest might best be served thereby;
* 3.8. safeguard confidential information in relation to his employer or client and not disclose such information to third parties without his employer's or client's written consent. A member shall not receive any gift, entertainment, payment or service from third parties for disclosing such information nor make use of it for personal gain.

---===---

# Rule 4: Responsibility to the Public

A member of the Institution in discharging his responsibilities to his employer and the profession shall at all times be governed by the overriding interest of the general public, in particular their environment, welfare, health and safety.

In pursuance of this rule a member shall, inter alia:

* 4.1. seek to protect the safety, health and welfare of the public;
* 4.2. when making a public statement professionally, try to ensure that both his qualification to make the statement and his association with any benefiting party are made known to the recipients of the statement;
* 4.3. seek to extend public understanding of the engineering profession;
* 4.4. seek to assess the environmental consequences of work for which he is responsible and to influence events so as to prevent or minimise damage to, and if practicable to improve, the environment.

In particular, in the exercise of the requirement to safeguard the public in matters of welfare, health and safety, engineers should:

* a) strive to create through their projects a healthy and agreeable outdoor and indoor environment;
* b) aim to minimise the use of non-renewable resources, to conserve energy and to minimise the generation of waste;
* c) consider and take into account the consequences of any proposal upon public health and local custom;
* d) assess the impacts of their proposals upon the environment, and select options that will ensure sustainable development;
* e) consider and explain in their proposals the measures required to protect and improve the environment;
* f) promote the concepts of interdependence of ecosystems, maintenance of the diversity of species, resource replacement and recovery, and sustainable development;
* g) seek to balance costs with the best benefit to the environment and to human society, to achieve the most suitable practical environmental option, by utilising the best available technology and techniques without entailing excessive cost;
* h) encourage management to follow positive environmental policies by recognising that a statement of intent is not sufficient to achieve legislative compliance.
"""

WFEO_markdown = """
# 1. DEMONSTRATE INTEGRITY 
## 1.1 Refrain from fraudulent, corrupt or criminal practices 
Corruption is “the abuse of power to obtain personal gain”. Corruption is not limited to money or 
goods. It might be to gain fame or popularity or boost an ego. Combating the disastrous effects of 
corruption in the global engineering and construction industry is a top priority because if corruption 
can be diminished, the poor of the world will be helped most. 
Taking a bribe in an infrastructure contract equates to stealing a road!  It means that less money is 
available for the provision of the infrastructure itself.  Similarly, corrupt or unreasonable industrial 
practices are a form of corruption, as they also reduce the amount of infrastructure that can be 
provided for a given amount of money. 
In practice, engineers must exhibit a zero tolerance attitude to fraudulent, corrupt or criminal 
practices. This means: 

* a) not engaging in misleading or deceptive conduct such as succumbing to the wrong influence. 
* b) neither soliciting nor accepting financial or other considerations, including free engineering designs, from material or equipment suppliers for specifying their products. 
* c) not accepting compensation, financial or otherwise, from the engaging party for services on the same project, nor providing free services, unless the circumstances are fully disclosed to, and agreed to, by all interested parties. 
* d) neither paying offering nor receiving, directly or indirectly, inducements to secure work. 
* e) informing an employer or client of any possible adverse consequences of proposed activities based on the accepted engineering practices of the day. 
* f) reporting unethical engineering activity undertaken by other engineers or non-engineers. This 
extends to include for example, situations in which senior officials of a firm make “executive” 
decisions which clearly and substantially alter the engineering aspects of the work, or protection of 
the public welfare or the environment arising from the work. 

## 1.2 Be objective and truthful 
Honesty, integrity, continuously updated competence, devotion to service and dedication to 
enhancing the life quality of society are cornerstones of professional responsibility. Within this 
framework, you should be objective and truthful and include all known and pertinent information on 
professional reports, statements and testimony.  
In practice, This means: 

* a) endeavouring to interpret engineering issues to the public in an objective and truthful manner. 
* b) applying your skills and knowledge with honesty, good faith and without personal bias. 
* c) ensuring that your privileged and trusted position in the community is not used for personal or 
sectional interests to the detriment of the wider community. 
* d) revealing the existence of any interest, financial or otherwise, that might affect or give the 
appearance of affecting your judgment in any matter about which you are making a statement 
or giving evidence.  

## 1.3 Practise fairly and with good faith towards clients, colleagues and others  
As an engineer, you have a responsibility to provide loyal service to your clients and employers for 
whom you should apply your knowledge and skills with fairness, honesty and in good faith. You 
have an obligation to exercise fairness in dealing with others and to provide support and assistance 
when required. This includes engaging, or advising to engage, experts or specialists when such 
services are deemed to be in the client’s or employer’s best interests. 
In practice, This means: 
 
* a) giving credit where it is due.  
* b) accepting, as well as giving, honest and fair professional criticism when commenting on 
another’s work or making public comment. 
* c) not revealing facts, data or information obtained in a professional capacity without the prior 
consent of its owner. 
* d) advising your clients or employers when you judge that a project will not be viable, whether on 
the basis of commercial, technical, environmental or any other such risk which you might 
reasonably have been expected to consider.  
* e) avoiding any actions or statements which can be construed as being unfairly critical of a 
colleague or intended to favour your own position at the expense of a colleague. 

---===---

# 2. PRACTISE COMPETENTLY 
## 2.1 Practise in a careful and diligent manner in accordance with their areas of competence  
There are three key components to engineering practice, with the Code of Ethics being just one of 
those components.  The other two key components are competence and performance.   
The Code of Ethics defines what it means to be a professional and sets standards of behaviour, 
competence refers to the ability to perform the activities within an occupation to the standards 
expected in employment and performance is associated with how these activities ought to be 
carried out or accomplished in an effective manner.   
You need to understand the distinction between working or providing advice in an area of 
competence and working competently.  Working in an area of competence requires you to operate 
within the limits of your qualifications and experiences.  Working competently requires principally 
the application of sound judgment.   
In practice, This means: 

* a) exercising care and communicating clearly in accepting or interpreting assignments, and in 
setting expected outcomes. 
* b) informing employers or clients, and making appropriate recommendations on obtaining further 
advice, if an assignment requires qualifications and experiences outside your fields of 
competence. 
* c) presenting issues fairly, accurately and with appropriate qualifiers and disclaimers, and to 
avoid personal, political and other non-technical biases. 
* d) expressing opinions on engineering issues honestly and only in areas of your competence. 
* e) reporting or advising on professional matters honestly and only in areas of your competence. 
* f) 
attaining and maintaining competence in all areas of involvement including being 
knowledgeable with the technical and legal framework and regulations governing your work. 

## 2.2 Practise in accordance with accepted engineering practices, standards and codes 
The work you undertake will be subject to various statutory regulations and compliance issues. 
It is important that you identify what codes and/or standards of compliance and/or legislation you 
are required to adhere to in respect of a particular project.  This should form part of the Brief, which 
should also allocate responsibility for such compliance.  Where statutory codes do not exist, it may 
be necessary to develop appropriate standards based on internationally recognised sound practice. 
In practice, This means: 
 
* a) Developing a checklist of relevant codes - before each project (and during each project) review 
the relevance and compliance with each code identified. 
* b) Examining legislative impacts - seek external assistance to identify what legislation is peculiar 
to this project  
* c) Reviewing Occupational Health & Safety issues - consider anything peculiar relating to this 
project; address with the client any observations of unsafe work practices noted during site 
visits - this may not be your responsibility yet you may be held partially liable if you fail to make 
such comments. 
* d) Ensuring Sub Consultant Compliance - obtain evidence of current compliance with OH&S 
legislation and other code and legislative obligations. 

## 2.3 Maintain and strive to enhance the body of knowledge in which they practice 
The requirement to practice within one’s area of competence is more than simply duty to a standard 
of care. Engineers have a responsibility to remain abreast of developments and knowledge in their 
area of expertise, that is, to maintain their own competence.  Should there be a technologically 
driven or individually motivated shift in the area of practice, it is the engineer’s duty to attain and 
maintain competence in all areas of involvement including being knowledgeable with the technical 
and legal framework and regulations governing their work.  
In practice, This means: 
 
* a) having a commitment to ongoing professional development, continuing education and training. 
* b) not falsifying or misrepresenting one’s own or an associates’ qualifications, grades of 
membership, experience and responsibilities. 
* c) striving to contribute to the advancement of the body of knowledge within which you practice, 
and to the profession in general. 
* d) assessing and responding to the range and availability of professional knowledge, 
competencies and resources required to undertake the engineering project and assessing any 
material uncertainties in these respects.  

---===---
# 3. EXERCISE LEADERSHIP 
## 3.1 Practise so as to enhance the quality of life in society 
Engineers are sometimes perceived by many in the community as being major contributors to many 
of the problems in the world, particularly environmental.  Having been painted with that brush, 
engineers are expected to be fundamental in solving or correcting those problems.  
But the major problems of the world in an overall sense are not those created by engineers or that 
can be solved by engineers alone.  War, greed, misery, ignorance and political interference, plus 
natural disasters and human induced pollution and destruction of resources are in fact the main 
causes of the progressive impairment of the environment.   
Rarely do major problems in society turn solely upon the application of engineering development.  
But engineers are active members of society and ought to be deeply involved in the promotion of 
sustainable development.  They ought to use their talent, knowledge and imagination to assist 
society in removing those evils and improving the quality of life for all people.   
In practice, This means: 

* a) aiming to deliver outcomes that do not compromise the ability of future life to enjoy the same or 
better environment, health, wellbeing and safety as currently enjoyed. 
* b) being sensitive to public concerns.  
* c) promoting the involvement of all stakeholders and the community in decisions and processes 
that may impact upon them and their environment. 
* d) in identifying sustainable outcomes considering all options in terms of their economic, 
environmental and social consequences. 

## 3.2 Strive to contribute to the advancement of the body of knowledge within which they practice, and to 
the profession in general 
A Code of Ethics is based on shared values and a shared responsibility to uphold those values.   
In practice, This means: 

* a) exercising fairness in dealing with others and providing support and assistance when required. 
* b) offering services, advising on or undertaking engineering assignments in areas of your competence 
by virtue of your training and experience. 
* c) participating, within the framework of the practice of your profession, in providing opportunities to 
further the professional development of your colleagues. 

## 3.3 Foster the public’s understanding of technical issues and the role of engineering 
As engineers we possess knowledge and skills on which others rely.  Our future is ultimately 
dependent on engagement and trust from our community.  It is important that we meet these 
community expectations by practising in ways which maintain and enhance community trust in the 
values and expertise of the engineering profession. 
When clients or others question your reasoning, or otherwise request an explanation, there is an 
expectation that you will be willing and able to explain why you have arrived at your particular 
outcome, especially as checking and justifying what we do are embedded in the way the 
engineering task develops.  
The notion of explaining one’s reasoning and seeking peer review is thought by many to be 
fundamental to professional integrity, but in no way denies the appropriateness of legitimate 
differences of reasoned opinion arrived at in a proper and professional manner.   
In practice, This means: 

* a) endeavouring to ensure that information provided to the public is relevant and in a readily 
understood form. 
* b) applying sound engineering judgment based on experience and relevant analysis to arrive at 
the appropriate balance of considerations in any given situation. 
* c) taking reasonable steps to understand the consequences of your actions and the actions of 
those working with or for you. 
* d) displaying restraint in the manner in which you comment on engineering matters, especially in 
circumstances where, by explicit reference or implication, there is a reason for the public to 
believe that such comments are made on the basis of relevant knowledge. 

---===---
# 4. PROTECT THE NATURAL AND BUILT ENVIROMENT  
## 4.1 Create and implement engineering solutions for a sustainable future 
Issues regarding the environment and sustainable development know no geographical boundaries.  
Sustainability is not just about the environment, but also about sustaining our social and economic 
future.  It is not about targets, or quotas, but about strategies.  It is not just about technologies, but 
also about transitional processes.  No matter how progressive the innovations in management and 
technology, they can only move society so far towards sustainability.  Modification of consumption 
behaviour, integrating political and societal aspirations and policies, and advancing the knowledge 
and skills to enhance the protection and restoration of natural systems all remain important issues 
to be addressed.   
Sustainable development is the challenge of meeting current human needs for natural resources, 
industrial products, energy, food, transportation, shelter, and effective waster management while 
conserving and, if possible, enhancing the Earths’ environmental quality, natural resources, ethical, 
intellectual and working affectionate capabilities of people and socioeconomic bases, essential for 
the human needs of future generations.  
Growth in demand and the use of non-renewable energy resources is creating important 
environmental challenges around the world.  These challenges range from a mixture of local or 
regional environmental concerns such as land degradation, water quality, waste management and 
urban air quality to global environmental dilemmas such as GHG emissions and the inter
connected occurrence of global warming.   
In practice, This means: 

* a) being aware that the principles of eco-systemic interdependence, diversity maintenance, 
resource recovery and inter-relational harmony form the basis of humankind’s continued 
existence and that each of these poses a threshold of sustainability that should not be 
exceeded. 
* b) discussing in particular the consequences of proposals and actions, direct or indirect, 
immediate or long term, upon the health of people, social equity and the local system of 
values. 
* c) promoting a clear understanding of the actions required to restore and, if possible, to improve 
the environment that may be disturbed, and include them in your proposals. 

## 4.2 Be mindful of the economic, societal and environmental consequences of actions or projects  
Proper observance of the principles of sustainable development will help considerably to eradicate 
world poverty. Sustainability is a system or process which can be maintained indefinitely and which 
revolves around integrating conservation and development on a long-term basis to provide social 
and economic benefits, without compromising the needs of future generations.  Engineers of all 
nations should know and respect the environmental ethics.   
In practice, This means: 

* a) making sure that your own perception of environmental issues is as accurate as possible. 
* b) striving to accomplish the beneficial objectives of your work with the lowest possible 
consumption of raw materials and energy and the lowest production of wastes and any kind of 
pollution. 
* c) studying the environment that will be affected by your work, assessing the impacts that might 
arise in the structure, dynamics and aesthetics of the ecosystems involved - urbanised or 
natural - as well as pertinent socioeconomic systems, and selecting the best alternative for 
development that is both environmentally sound and sustainable. 
* d) rejecting any kind of commitment that involves unfair damages to human surroundings and 
nature and aim for the best possible technical, social and political solution. 
* e) being aware of and making sure that clients and employers are aware of societal and 
environmental consequences of actions or projects and endeavouring to interpret engineering 
issues to the public in an objective and truthful manner. 

## 4.3 Promote and protect the health, safety and well being of the community and the environment 
The obligation to protect the health, safety and well being of the community is often dependent on 
engineering judgments, risk assessments, decisions and practices incorporated into structures, 
machines, product, processes and devices.  Engineers ought to control and make sure that what 
they are involved with conforms to accepted engineering practices, standards and applicable 
codes, and would be considered safe based on peer adjudication.   
Laudable though the aim of acting in the interests of the community above all else might be, there 
is a danger in making simplistic statements that say categorically that our duties and responsibilities 
lie in only one direction, implying by such statements that we have a duty to override (and not 
balance) legal, fiduciary and contractual responsibilities if they conflict with that ‘grand’ duty.  
In practical terms, those legal duties and obligations will arise principally in two specific contexts.  
First, there will be duties and obligations of engineers to their clients.  Second, there will be duties 
and obligations of those engineers who are employees to their employers.  In some cases there 
may be a conflict/tension between legal duties and ethical obligations.  
Engineers who have reason to believe that there is a threat to public health and safety as a result of 
an engineering activity, or its products, processes etc. not conforming to the above stated 
conditions ought to bring the matter to the attention of the relevant authority. 
In practice, This means: 

* a) having due regard for the health, safety and wellbeing of the public and fellow employees in all 
work for which they are responsible. 
* b) trying with the best of their ability, courage, enthusiasm and dedication to obtain a superior 
technical achievement which will contribute to and promote a healthy and agreeable 
surrounding for all people, in open spaces as well as indoors. 
* c) informing your employer or contractor of the possible consequences if your recommendations 
on issues of safety, health, welfare or sustainable development are overruled or ignored. 


"""

AIAA_markdown = """
# General Ethical Expectations

## A. Hold paramount the safety, health, and welfare of the public in the performance of their duties.
Examples/Elaborations include but are not limited to the following:

* Recognize that the lives, safety, health, and welfare of the public are dependent upon professional judgments, decisions, and ethical practices.
* Report suspected violations of this element of the code to the proper authority and cooperate in furnishing further information and assistance as required.

---===---
# Professional Integrity

## B. Avoid real and perceived conflicts of interest.
Examples/Elaborations include but are not limited to the following:

* Ensure that technical contributions are not compromised or biased by a conflict of interest or other inappropriate influences.
* Inform employers, clients, or other professional associates of any relationships, interests, or circumstances that could influence, or could be perceived to influence, your judgment.
* Issue no statements, criticisms, arguments, or professional opinions that are paid for by interested parties, unless it is indicated on whose behalf those statements are made.
* Avoid any appearance of impropriety.
## C. Act as an honest and fair agent in all professional interactions.
Examples/Elaborations include but are not limited to the following:

* Protect the proprietary interests or confidences concerning the business affairs or technical processes of current and former employers, clients, and colleagues except where disclosure or reporting is required by law, or consent granted.
* Charge fairly for services rendered and fulfill obligations as agreed – honoring contracts, agreements, and assigned responsibilities.
* Do not accept compensation, financial or otherwise, from more than one party for the same service without the consent of all interested parties.
## D. Reject bribery, fraud, and corruption in all their forms and avoid unlawful conduct in professional activities.
Examples/Elaborations include but are not limited to the following:

* Comply with public law and regulation.
* Do not knowingly engage in business or professional practices of a fraudulent, dishonest, or unethical nature.
## E. Properly credit the contributions of others, accept and offer honest and constructive criticism of technical work, and acknowledge and correct errors promptly.
Examples/Elaborations include but are not limited to the following:

* Acknowledge and recognize the contributions of colleagues, taking care that credit for professional work and accomplishments are given to those to whom credit is properly due.
* Accurately present and explain one’s work and its merit and avoid any act that would promote personal interests at the expense of the integrity, honor, and dignity of the profession.
* Do not maliciously or indiscriminately criticize the work of another.
* Perform comprehensive and thorough evaluations of technical work, addressing potential impacts and including analysis of possible risks.
## F. Issue statements or present information in an objective and truthful manner, based on available data.
Examples/Elaborations include but are not limited to the following:

* Reject all forms of research or testing misconduct and report all misconduct including fabrication, falsification, and plagiarism when it is observed.
* Do not disseminate misleading, unsubstantiated, or exaggerated claims regarding technical matters.
* Be objective, truthful, and complete in professional statements, professional reports, or expert testimony.
* Express professional opinions only when founded on a background of technical competence.
* In speaking or writing, do not infer in any way that you are doing so on behalf of an organization (including AIAA) unless explicitly authorized to do so.
## G. Undertake only those tasks for which one is qualified by training or experience, or for which one can reasonably become qualified with proper preparation, education, and training.
Examples/Elaborations include but are not limited to the following:

* Do not perform engineering services dealing with subject matter outside areas of expertise by virtue of education or experience.
* Do not falsify or permit misrepresentation of academic or professional qualifications or experience.
 
---===---
# Personal Conduct

## H. Treat all persons with respect, fairness, and dignity, and never engage in any form of harassment or discrimination.
Examples/Elaborations include but are not limited to the following:

* Equally treat all persons fairly and with respect without regard to race, color, creed, gender, religion, age, national origin, citizenship status, veteran status, marital status, sexual orientation, gender identify, gender expression, disability, or any other protected status.
* Never engage in any form of harassment, whether verbal, visual, or physical, including sexual harassment or bullying.
* Promote fair and unbiased opportunities for all.
## I. Avoid harming others, their property, their reputations, or their employment through false or malicious statements or through unlawful or otherwise wrongful actions.
Examples/Elaborations include but are not limited to the following:

* Do not maliciously injure the professional reputation, prospects, or practice of another.
* Protect the proprietary interests or confidences concerning the business affairs or technical processes of current and former employers and colleagues except where disclosure or reporting is required by law, or consent granted.
* Do not retaliate against those who make lawful reports about contraventions of law, regulation, health, or safety.
 
"""

# there is a shortcode lookup for the image

# HKIE: H1.1 as an example for HKIE_rule1.1.png
# AIAA: A1.1 as an example for AIAA_rule1.1.png
# WFEO: W1.1 as an example for WFEO_rule1.1.png

# generate the shortcodes and their corresponding image names by scanning the output folder

from glob import glob
import os

# Get the list of image files in the output folder
image_files = glob("output/*.png")

shortcodes = {}

for image_file in image_files:
    # Get the image name
    image_name = os.path.basename(image_file)
    
    # Get the rule name
    rule_name = image_name.split("_")[1]
    
    # Get the organization name
    organization_name = image_name.split("_")[0]
    
    # Get the shortcode
    shortcode = organization_name[0] + rule_name.replace("rule", "").replace(".png", "")
    
    # Add the shortcode to the dictionary
    shortcodes[shortcode] = image_name
    
print(shortcodes)

@ui.page("/")
def page():
    
    # Event handler for the button
    def display_image():
        # Get the text from the input
        shortcode_in = text_input.value
        
        # Try to display the image from the output folder using the shortcode
        
        if not shortcode_in:
            text_guidance.set_text("Start with one of H (HKIE), A (AIAA), or W (WFEO)")
            return
        
        if shortcode_in[0] in ("H", "A", "W"):
            if len(shortcode_in) == 1:
                # list numbers the user can enter by going through the shortcodes and finding the ones that start with the organization code and tfirst second character is a number
                options = sorted(list(set([shortcode[1] for shortcode in shortcodes.keys() if shortcode.startswith(shortcode_in)])))
                text_guidance.set_text(f"Enter the rule number: {', '.join(options)}")
        else:
            text_guidance.set_text("Invalid shortcode")
            image_container.set_source("assets/empty.png")
            image_container.force_reload()
            return
        
        if len(shortcode_in) >= 2:
            # list options available in shortcode which begins with shortcode_in
            options = [shortcode for shortcode in shortcodes.keys() if shortcode.startswith(shortcode_in) or shortcode == shortcode_in]

            # if exact match is found, display the image
            if shortcode_in in shortcodes:
                image_name = shortcodes[shortcode_in]
                image_path = f"output/{image_name}"
                image_container.set_source(image_path)
                image_container.force_reload()
                
                
            if len(options) >= 1:
                text_guidance.set_text(f"Options available: {', '.join(options)}")
            else:
                text_guidance.set_text("No results")
                image_container.set_source("assets/empty.png")
                image_container.force_reload()
                # remove the last character from the input
                # text_input.set_value(text_input.value[:-1])
                
            print(options)
    
        if len(shortcode_in) >= 2:
            #second character is a number
            # open the respective markdown section splitted by ---===--- and display the rule
            
            if shortcode_in[1].isdigit():
                rule_number = shortcode_in[1]
                if shortcode_in[0] == "H":
                    if shortcode_in in shortcodes:
                        # since there is a singular match, do the following
                        # for all lines beginning with a *, include it if the line without the * stripped of whitespace
                        # starts with the rule number
                        def is_line_relevant(line):
                            criteria = [len(line) < 1 or line[0] != "*", line.replace("*", "").strip().startswith(shortcode_in[1:]+".")]
                            print(line, criteria)
                            return any(criteria)
                        filtered_content = [line for line in HKIE_markdown.split("---===---")[int(rule_number)-1].splitlines() if is_line_relevant(line)]
                        markdown_container.content = "\n".join(filtered_content)
                    else:
                        markdown_container.content = (HKIE_markdown.split("---===---")[int(rule_number)-1])
                elif shortcode_in[0] == "W":
                    if shortcode_in in shortcodes:
                        # this time, the filtering logic has to do with ##, and affects the entire block (use splitby ##)
                        def is_block_relevant(block):
                            return block.strip().startswith(shortcode_in[1:]+" ")
                        filtered_content = [block for i, block in enumerate(WFEO_markdown.split("---===---")[int(rule_number)-1].split("## ")) if i==0 or is_block_relevant(block)]
                        markdown_container.content = "## ".join(filtered_content)
                    else:
                        markdown_container.content = (WFEO_markdown.split("---===---")[int(rule_number)-1])
                elif shortcode_in[0] == "A":
                    if shortcode_in in shortcodes:
                        # this time, the filtering logic has to do with ##, and affects the entire block (use splitby ##)
                        def is_block_relevant(block):
                            print(block)
                            return block.strip().startswith(shortcode_in.split(".")[1]+".")
                        filtered_content = [block for i, block in enumerate(AIAA_markdown.split("---===---")[int(rule_number)-1].split("## ")) if i==0 or is_block_relevant(block)]
                        markdown_container.content = "## ".join(filtered_content)
                    else:
                        markdown_container.content = (AIAA_markdown.split("---===---")[int(rule_number)-1])

    ui.label("LANG2030 Interactive Codes Online (ICO) system").classes("text-2xl font-bold")
    
    ui.label("Copyright 2024, Evan (online username: evnchn). All rights reserved.")
    # Create the image container
    
    with ui.card().classes("w-full"):
        image_container = ui.image()

    # Create the layout
    with ui.row():
        # Text input
        text_input = ui.input(placeholder="Enter shortcode", on_change=display_image)

        # Button to display the image
        display_button = ui.button("Display Image", on_click=display_image)
        
    text_feedback = ui.label("Enter rule code (e.g. H1.1, A1.1, W1.1) to display the image.")

    text_guidance = ui.label("")
    
    image_container.set_source("assets/empty.png")
    image_container.force_reload()
    
    markdown_container = ui.markdown("")
    
    display_image()


            
            
        
        
        





ui.run()