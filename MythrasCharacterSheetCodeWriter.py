class skill:
    def __init__(self, f_id, f_label, f_base, f_category = "standard"):
        self.id = f_id
        self.label = f_label
        self.base = f_base
        self.category = f_category
    #

    def add_cells(self, f_string):
        return_string = f_string + str("            <tr>\n" + 
                                       "                <td>" + self.label + "</td>\n" +    #label
                                       "                <td>" + self.base + "</td>\n" +     #base characteristics (description)
                                       "                <td>" +                             #checkbox
                                       "<input  {% if variables." + self.id + "_checkbox is defined and variables." + self.id + "_checkbox == 1   %} " +
                                       "checked='checked'{% endif %} " +
                                       "{% if variables." + self.id + "_checkbox is defined and variables." + self.id + "_checkbox == 0   %} " +
                                       "checked='unchecked'{% endif %} " +
                                       "class='' id='" + self.id + "_checkbox' name='" + self.id + "_checkbox' placeholder='' type='checkbox' align='center'/>" +
                                       "</td>\n" +
                                       "                <td>" +                             #percentage value
                                       "<input id='" + self.id + "' class='form-control' name='" + self.id + 
                                       "' type='number' value='{{ variables." + self.id + 
                                       " is defined ? variables." + self.id + " }}' placeholder='' /></td>\n" +
                                       "                <td>" +                             #notes string field
                                       "<input id='" + self.id + "_notes' class='form-control' name='" + self.id + 
                                       "_notes' type='text' value='{{ variables." + self.id + 
                                       " is defined ? variables." + self.id + "_notes }}' placeholder='' /></td>\n" +
                                       "            </tr>\n")
        return return_string
#

#build skills
skills = [
    skill("athletics", "Athletics", "Str + Dex"),                           #standard
    skill("boating", "Boating", "Str + Con"),
    skill("conceal", "Conceal", "Dex + Pow"),
    skill("customs", "Customs", "Int x2"),
    skill("dance", "Dance", "Dex + Cha"),
    skill("deceit", "Deceit", "Int + Cha"),
    skill("drive", "Drive", "Dex + Pow"),
    skill("first_aid", "First Aid", "Int + Dex"),
    skill("influence", "Influence", "Cha x2"),
    skill("insight", "Insight", "Int + Pow"),
    skill("locale", "Locale", "Int x2"),
    skill("perception", "Perception", "Int + Pow"),
    skill("ride", "Ride", "Dex + Pow"),
    skill("stealth", "Stealth", "Dex + Int"),
    skill("swim", "Swim", "Str + Con"),
    skill("unarmed", "Unarmed", "Str + Dex"),
    skill("brawn", "Brawn", "Str + Siz", "resistance"),                     #resistances
    skill("endurance", "Endurance", "Con x2", "resistance"),
    skill("evade", "Evade", "Dex x2", "resistance"),
    skill("willpower", "Willpower", "Pow x2", "resistance"),
    skill("acting", "Acting", "Cha x2", "professional"),                    #prof skills
    skill("acrobatics", "Acrobatics", "Str + Dex", "professional"),
    skill("art", "Art", "Cha + Pow", "professional"),
    skill("bureaucracy", "Bureaucracy", "Int x2", "professional"),
    skill("commerce", "Commerce", "Int + Cha", "professional"),
    skill("courtesy", "Courtesy", "Int + Cha", "professional"),
    skill("craft", "Craft", "Dex + Int", "professional"),
    skill("culture", "Culture", "Int x2", "professional"),
    skill("disguise", "Disguise", "Int + Cha", "professional"),
    skill("engineering", "Engineering", "Int x2", "professional"),
    skill("gambling", "Gambling", "Int + Pow", "professional"),
    skill("healing", "Healing", "Int + Pow", "professional"),
    skill("language", "Language", "Int + Cha", "professional"),
    skill("literacy", "Literacy", "Int x2", "professional"),
    skill("lockpicking", "Lockpicking", "Dex x2", "professional"),
    skill("lore", "Lore", "Int x2", "professional"),
    skill("mechanisms", "Mechanisms", "Dex + Int", "professional"),
    skill("musicianship", "Musicianship", "Dex + Cha", "professional"),
    skill("navigation", "Navigation", "Int + Pow", "professional"),
    skill("oratory", "Oratory", "Pow + Cha", "professional"),
    skill("seamanship", "Seamanship", "Int + Con", "professional"),
    skill("seduction", "Seduction", "Int + Cha", "professional"),
    skill("sleight", "Sleight", "Dex + Cha", "professional"),
    skill("streetwise", "Streetwise", "Pow + Cha", "professional"),
    skill("survival", "Survival", "Con + Pow", "professional"),
    skill("teach", "Teach", "Int + Cha", "professional"),
    skill("track", "Track", "Int + Con", "professional"),
    skill("binding", "Binding", "Cha + Pow", "magic"),                      #magic skills
    skill("devotion", "Devotion", "Cha + Pow", "magic"),
    skill("exhort", "Exhort", "Int + Cha", "magic"),
    skill("folk_magic", "Folk Magic", "Cha + Pow", "magic"),
    skill("invocation", "Invocation", "Int x2", "magic"),
    skill("meditation", "Meditation", "Int + Con", "magic"),
    skill("mysticism", "Mysticism", "Pow + Con", "magic"),
    skill("shaping", "Shaping", "Int + Pow", "magic"),
    skill("trance", "Trance", "Pow + Con", "magic")
    ]

#pre-skill html
html_start = str(open("html_start.html", mode='r').read())
#print(html_start)

#standard skills html
html_string = str(html_start + "\n\n" +
                  "    <h2>Standard Skills</h2>\n" +
                  "    <table>\n" + 
                  "        <tbody>\n" + 
                  "            <tr>\n" + 
                  "                <td><h4>Skill</h4></td><td><h4>Base %</h4></td><td><h4>Culture/Career</h4></td><td><h4><center>%</center></h4></td>\n<td><h4>Notes</h4></td>\n" + 
                  "            </tr>\n")


for each_skill in skills:
    if each_skill.category == "standard":
        html_string = each_skill.add_cells(html_string)
    #
#

html_string = html_string + str("        </tbody>\n    </table>\n\n")


#resistances html
html_string = html_string + str("    <h2>Resistances</h2>\n" +
                                "    <table>\n" + 
                                "        <tbody>\n" + 
                                "            <tr>\n" + 
                                "                <td><h4>Skill</h4></td><td><h4>Base %</h4></td><td><h4>Culture/Career</h4></td><td><h4><center>%</center></h4></td>\n<td><h4>Notes</h4></td>\n" + 
                                "            </tr>\n")

for each_skill in skills:
    if each_skill.category == "resistance":
        html_string = each_skill.add_cells(html_string)
    #
#

html_string = html_string + str("        </tbody>\n    </table>\n\n")


#professional skills html
html_string = html_string + str("    <h2>Professional Skills</h2>\n" +
                                "    <table>\n" + 
                                "        <tbody>\n" + 
                                "            <tr>\n" + 
                                "                <td><h4>Skill</h4></td><td><h4>Base %</h4></td><td><h4>Culture/Career</h4></td><td><h4><center>%</center></h4></td>\n<td><h4>Notes</h4></td>\n" + 
                                "            </tr>\n")

for each_skill in skills:
    if each_skill.category == "professional":
        html_string = each_skill.add_cells(html_string)
    #
#

html_string = html_string + str("        </tbody>\n    </table>\n\n")


#magic skils html
html_string = html_string + str("    <h2>Magic Skills</h2>\n" +
                                "    <table>\n" + 
                                "        <tbody>\n" + 
                                "            <tr>\n" + 
                                "                <td><h4>Skill</h4></td><td><h4>Base %</h4></td><td><h4>Culture/Career</h4></td><td><h4><center>%</center></h4></td>\n<td><h4>Notes</h4></td>\n" + 
                                "            </tr>\n")

for each_skill in skills:
    if each_skill.category == "magic":
        html_string = each_skill.add_cells(html_string)
    #
#

html_string = html_string + str("        </tbody>\n    </table>\n\n")


#end html
html_string = html_string + str("</div>")






#generate YAML for skills
yaml_string = str("fields:\n")
for each_skill in skills:
    yaml_string = yaml_string + str("  " + each_skill.id + ":\n" + #% value
                                    "    input: integer\n" +
                                    "    label: " + each_skill.label + "\n" +
                                    "    description: " + each_skill.base + "\n" +
                                    "    min: 0\n" +
                                    "  " + each_skill.id + "_checkbox:\n" + #culture/prof checkbox
                                    "    input: checkbox\n" +
                                    "    label: " + each_skill.label + " Checkbox\n" +
                                    "  " + each_skill.id + "_notes:\n" + #notes string field
                                    "    input: string\n" +
                                    "    label: " + each_skill.label + " Notes\n")


print(html_string)
print("\n\n" + ("="*40) + "\n\n")
print(yaml_string)
print("\n\n" + ("="*40) + "\n\n")
#print(yaml_prof)