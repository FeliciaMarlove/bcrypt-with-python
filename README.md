# bcrypt-with-python
Simple implementation of Bcrypt library with Python

## What you can do with this program
### generate_random_password(length)
Get a randomly generated password containing [length] caracters
### get_time_cost_changing_pwd_length(lower_bound, upper_bound)
Get a list of results, with first item as the length of the password, and second item as the time spent by Bcrypt to hash it. 
To calculate the time, his method generates random passwords using the above mentionned method, with length going from [lower_bound] to [upper_bound] included.
### get_time_cost_changing_rounds(lower_bound, upper_bound)
Get a list of results, with first item as the number of salt rounds, and second item as the time spent by Bcrypt to hash it. 
To calculate the time, his method generates generates a salt of [x], with rounds going from [lower_bound] to [upper_bound] included.
### get_user_powd_hash()
Ask user to input a password and return the hash (salt 16).
### check_pwd(hashed_pwd)
Check that the user input matches the previously recorded password.
### generate_salt(rounds=12)
Generate a salt of [rounds], defaulting to 12 rounds.
### hash_pwd(pwd, salt)
Generate a hash of the [pwd] with [salt].
### encode_password(pwd)
Encore the [pwd] as UTF-8.
### ask_password()
Ask for user input and return the value.
