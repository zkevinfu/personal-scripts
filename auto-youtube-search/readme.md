# auto-youtube-search
script to make the process of reviewing a list of songs on youtube easier

takes in a .txt datafile with the following structure

```
media name 1
song name 1
song name 2

media name 2
song name 1
song name 2

ENDFILE

metadata
more metadata
```

nothing after the first ENDFILE is looked at

outputs a .json file with the following structure

```
{
  media name 1:
    {
      song name 1:
        {
          self provided link,
          self provided desc
        },
        etc..
    },
    etc..
}
```

