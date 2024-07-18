# Password-Cracker

```markdown
# Password Cracker

This project is a password cracker implemented in Python. It supports both dictionary attacks and brute-force attacks to crack SHA-256 hashed passwords.

## Features

- **Dictionary Attack**: Uses a list of potential passwords from a dictionary file to find the correct password.
- **Brute-Force Attack**: Tries all possible combinations of characters up to a specified length to find the correct password.

## Project Structure

```
password_cracker/
├── dictionary.txt
└── password_cracker.py
```

- **`dictionary.txt`**: Contains a list of common passwords and potential candidates.
- **`password_cracker.py`**: Main script that implements the password cracking techniques.

## Prerequisites

- Python 3.x

## Usage

1. **Prepare the Dictionary File**:
   - Populate `dictionary.txt` with a list of potential passwords, each on a new line.

2. **Run the Script**:
   - Execute the `password_cracker.py` script using Python:

     ```bash
     python password_cracker.py
     ```

3. **Customize Attacks**:
   - Adjust the `dictionary_file` path and content based on your needs.
   - Modify `brute_force_attack` parameters (`max_length`, `characters`) to suit your scenario.

## Example

### Dictionary Attack

Given a hashed password, the script will attempt to find the original password using a dictionary attack:

```python
hashed_password = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
```

### Brute-Force Attack

If the dictionary attack fails, the script will attempt to find the original password using a brute-force attack:

```python
result = brute_force_attack(hashed_password, max_length=4)
```

## Enhancements

- **Parallel Processing**: Use `multiprocessing` for faster processing, especially in the brute-force attack.
- **Optimization**: Optimize the dictionary attack with memory-efficient techniques for large dictionaries.
- **Advanced Attacks**: Implement hybrid attacks combining dictionary and brute-force methods.

## Legal and Ethical Considerations

- Ensure you have permission to perform password cracking activities on the target system or data.
- Do not use real passwords or perform attacks on systems without explicit authorization.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various open-source security tools and educational resources.
```

This `README.md` provides a clear overview of the project, its features, usage instructions, and important considerations. It can be placed in the root directory of your project to help others understand and use your password cracker effectively.
