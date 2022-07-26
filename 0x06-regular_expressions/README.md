Regular Exep

Background Context


For this project, you have to build your regular expression using Oniguruma, a regular expression 

library that which is used by Ruby by default. Note that other regular expression libraries 

sometimes have different properties. Because the focus of this exercise is to play with regular 

expressions (regex), here is the Ruby code that you should use, just replace the regexp part,

meaning the code in between the //:

        sylvain@ubuntu$ cat example.rb
        
        #!/usr/bin/env ruby
        
        puts ARGV[0].scan(/127.0.0.[0-9]/).join
        
        sylvain@ubuntu$
        
        sylvain@ubuntu$ ./example.rb 127.0.0.2
        
        127.0.0.2
        
        sylvain@ubuntu$ ./example.rb 127.0.0.1
        
        127.0.0.1
        
        sylvain@ubuntu$ ./example.rb 127.0.0.a


Requirements

General

  * Allowed editors: vi, vim, emacs

  * All your files will be interpreted on Ubuntu 20.04 LTS

  * All your files should end with a new line

  * A README.md file, at the root of the folder of the project, is mandatory

  * All your Bash script files must be executable

  * The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby

  * All your regex must be built for the Oniguruma library


0-simply_match_school.rb - The regular expression must match 'School'

Example:

  sylvain@ubuntu$ ./0-simply_match_school.rb School | cat -e
  
  School$
  
  sylvain@ubuntu$ ./0-simply_match_school.rb "Best School" | cat -e
  
  School$
  
  sylvain@ubuntu$ ./0-simply_match_school.rb "School Best School" | cat -e
  
  SchoolSchool$
  
  sylvain@ubuntu$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
  
  $
  
![image](https://user-images.githubusercontent.com/99422296/181104417-f9858c1a-4c79-43d1-ab96-b44f62e8a48a.png)


1-repetition_token_0.rb - Find the regular expression that will match the above cases

Using the project instructions, create a Ruby script that accepts one argument and pass it to a 

regular expression matching method


![image](https://user-images.githubusercontent.com/99422296/181104727-f857f6c6-70f5-44e6-896e-3bfa767a3e22.png)

2-repetition_token_1.rb - Find the regular expression that will match the above cases

Using the project instructions, create a Ruby script that accepts one argument and pass it to a 

regular expression matching method


![image](https://user-images.githubusercontent.com/99422296/181104934-7391b371-88ae-4eba-8f52-24ffc956f481.png)

3-repetition_token_2.rb - Find the regular expression that will match the above cases

Using the project instructions, create a Ruby script that accepts one argument and pass it to a 

regular expression matching method

![image](https://user-images.githubusercontent.com/99422296/181105064-d63d8bd0-c7c9-4a7c-9d17-2f7477ff974e.png)

4-repetition_token_3.rb - Find the regular expression that will match the above cases

Using the project instructions, create a Ruby script that accepts one argument and pass it to a 

regular expression matching method

Your regex should not contain square brackets


5-beginning_and_end.rb - The regular expression must be exactly matching a string that starts 

with h ends with n and can have any single character in between

Using the project instructions, create a Ruby script that accepts one argument and pass it to a 

regular expression matching method

  Example:

      sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
      $
      sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
      hbn$
      sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
      $
      sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
      h8n$
      sylvain@ubuntu$
      $


6-phone_number.rb - This task is brought to you by a professional advisor Neha Jain, Senior Software Engineer at LinkedIn.

      Requirement:

          * The regular expression must match a 10 digit phone number
      Example:

      sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
      
      4155049898$
      
      sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
      
      $
      
      sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
      
      $
      
      sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
      
      $
      
      sylvain@ubuntu$


7-OMG_WHY_ARE_YOU_SHOUTING.rb - The regular expression must be only matching: capital letters

      Example:

      sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft       
      vAnilla Dupper Mint Ice Nutella cream" | cat -e
      
      ILOVESYSADMIN$
      
      sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
      
      WHATSAY$
      
      sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
      
      $
      
      sylvain@ubuntu$


100-textme.rb - This exercise was prepared for you by Guillaume Plessis, VP of Infrastructure at TextMe. It is something he uses daily. You can thank Guillaume for his project on Twitter.

For this task, you’ll be taking over Guillaume’s responsibilities: one afternoon, a TextMe VoIP Engineer comes to you and explains she wants to run some statistics on the TextMe app text messages transactions.

      Requirements:

      * Your script should output: [SENDER],[RECEIVER],[FLAGS]
      * The sender phone number or name (including country code if present)
      * The receiver phone number or name (including country code if present)
      * The flags that were used
      * You can find a [log file here].

