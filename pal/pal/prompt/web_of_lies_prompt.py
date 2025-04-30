# Copyright 2022 PAL Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


WEB_OF_LIES_PROMPT = (
    """
# Generate Python3 Code to solve problems
Q: Fidel tells the truth. Jerry says Fidel tells the truth. Vina says Jerry tells the truth. Mill says Vina lies. Ray says Mill lies. Does Ray tell the truth?
Fidel = True
Jerry_says_Fidel = True
Vina_says_Jerry = True
Mill_says_Vina = False
Ray_says_Mill = False
Jerry = Jerry_says_Fidel == Fidel
Vina = Vina_says_Jerry == Jerry
Mill = Mill_says_Vina == Vina
Ray = Ray_says_Mill == Mill
answer = Ray

Q: Kris lies. Millie says Kris lies. May says Millie tells the truth. Fidel says May lies. Leda says Fidel lies. Does Leda tell the truth?
Kris = False
Millie_says_Kris = False
May_says_Millie = True
Fidel_says_May = False
Leda_says_Fidel = False
Millie = Millie_says_Kris == Kris
May = May_says_Millie == Millie
Fidel = Fidel_says_May == May
Leda = Leda_says_Fidel == Fidel
answer = Leda

Q: Erin tells the truth. Mich says Erin lies. Ray says Mich tells the truth. Oslo says Ray tells the truth. Jamey says Oslo tells the truth. Does Jamey tell the truth?
Erin = True
Mich_says_Erin = False
Ray_says_Mich = True
Oslo_says_Ray = True
Jamey_says_Oslo = True
Mich = Mich_says_Erin == Erin
Ray = Ray_says_Mich == Mich
Oslo = Oslo_says_Ray == Ray
Jamey = Jamey_says_Oslo == Oslo
answer = Jamey
  
Q: Alice tells the truth. Ben says Alice lies. Clara says Ben tells the truth. David says Clara tells the truth. Ella says David tells the truth. Does Ella tell the truth?
Alice = True
Ben_says_Alice = False
Clara_says_Ben = True
David_says_Clara = True
Ella_says_David = True
Ben = Ben_says_Alice == Alice
Clara = Clara_says_Ben == Ben
David = David_says_Clara == Clara
Ella = Ella_says_David == David
answer = Ella

Q: Jake tells the truth. Leo says Jake tells the truth. Mia says Leo lies. Nora says Mia tells the truth. Owen says Nora lies. Does Owen tell the truth?
Jake = True
Leo_says_Jake = True
Mia_says_Leo = False
Nora_says_Mia = True
Owen_says_Nora = False
Leo = Leo_says_Jake == Jake
Mia = Mia_says_Leo == Leo
Nora = Nora_says_Mia == Mia
Owen = Owen_says_Nora == Nora
answer = Owen

# Q: {question}
""".strip()
    + "\n"
)
