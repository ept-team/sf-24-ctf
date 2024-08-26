# SF CTF 2024 - Writeups
This is a repo collecting writeups from players for the challenges to the SF CTF 2024.

We want **YOU!** to submit your writeups as pull requests to this repo to gather everything in one place, instead of a messy #writeups channel on Discord.

## Structure
This repositoriy follows the following structure:
```
Category > Challenge Name >
 - README.md - Contains challenge name and description.
 - <files> - Any files provided by the challenge will be listed here
 Team name >
   - README.md
   - solve.py
   - <any other solve files needed>
```
So we have already provided a list of categories and challenges. Each challenge directory will contain a README.md with the challenge description and name. Any files provided by the challenge will be in the directory as well.

~~To update the root [README.md](../README.md) with your writeup, you need to add a link to your writeup. This can be done by running the [updateWriteups.py](../updateWriteups.py) script with the following command:~~

~~python3 updateWriteups.py~~

Edit: this is now done automatically, using a github action.

## Submitting your writeup
We then want you to submit your writeups in a folder with your team name. There you are free to add a README.md explaining your solution and any other solve scripts or files used to solve the challenge.

Please see the example write-up provided by the EPT team in 2022 inside [here](https://github.com/ept-team/equinor-ctf-2022/blob/main/writeups/Stego/Reversing/ept/README.md).

Submit one writeup per Pull Request to the repository. Simply put, create a fork of the repository and create a pull request from your fork. These resources might be usefull:
* [How to make a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
* [How to make a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)