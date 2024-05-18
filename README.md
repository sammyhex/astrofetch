<h1>Astrofetch: Fetch & display zodiac seasons</h1>
<h2 align=center>
  <img src="https://github.com/longtallsammy/astrofetch/assets/66911338/156d1a8c-2129-4a6b-817c-5eaa9bb0800f">
</h2>
<h3>A simple program which fetches information about the system and the current zodiac season. Unicode and widget-friendly, dates and signs are searchable!</h3>
<h2>Usage:</h2>
<details>
  <summary>Normal usage</summary>
  <p></p>
  <p>Display a logo of todays zodiac sign, some information about it, and fetch system specs.</p>
  <b>
    
    astrofetch
  
  </b>
</details>

<details>
  <summary>Single-line mode</summary>
  <p></p>
  <p>Omit logo and system specs; instead print the time, date, and season on a single line.</p>
  <b>
    
    astrofetch -s
  
  </b>
  <p><b>Output:</b>
    
  >   14:36, May 18, Taurus season.
    
  </p>
   <p><b>
    
   - Unicode mode

   </b></p>
  <p></p>
  <p>Return the current time, and the unicode symbol for the current zodiac season.</p>
  <b>

    astrofetch -s -u
    
  </b>
  <p><b>Output:</b>

  >  14:36 ♉
    
  </p>
</details>

<details>
  <summary>Mini mode</summary>
  <p></p>
  <p>Return the name of the current season, and nothing else.</p>
  <b>
    
    astrofetch -m
  
  </b>
  <p><b>Output:</b></p>
  <p>
    
  >   Taurus
       
  </p>
  <p><b>
    
   - Unicode mode

   </b></p>
  <p></p>
  <p>Return the current season as a unicode symbol instead of text.</p>
  <b>

    astrofetch -m -u
    
  </b>
  <p><b>Output:</b>

  >   ♉
    
  </p>
</details>

<details>
  <summary><u>Info mode</u></summary>
  <p></p>
  <p><b>Date search:</b></p>
  <p>Return what season a given date lies in.</p>
  <b>
    
    astrofetch -i jan 1
  
  </b>
  <p><b>Output:</b>
    
   >  Capricorn season runs from December 22 to January 19.
    
  </p>
  <p><b>
    
   - Unicode mode

  </b></p>
  <p><b>Sign search</b></p>
  <p></p>
  <p>Return the given date as a unicode symbol instead of text.</p>
  <b>

    astrofetch -i jan 1 -u
    
  </b>
  <p><b>Output:</b>

   >  ♑
    
  </p>
  <p>Return information about a given zodiac sign.</p>
  <b>

    astrofetch -i capricorn
    
  </b>
  <p><b>Output:</b>

   >  Capricorn season runs from December 22 to January 19.
   > 
   >  Planet: Saturn
   > 
   >  Element: Earth
   > 
   >  Modality: Cardinal
    
  </p>
 <p><b>  
   
   -  Unicode mode

  </b></p>
  <p></p>
  <p>Return the unicode symbol of the sign given, and show date range of the season.</p>
  <b>

    astrofetch -i capricorn -u
    
  </b>
  <p><b>Output:</b></p>
  
   >  ♑ Dec 22 -> Jan 19
    
</details>
<h2>Tips and Tricks:</h2>
<details>
  <summary>Set zodiac sign at command prompt</summary>
  <p>

    export PS1="$(astrofetch -i jan 1 -u) \u@\h: \W $ "
    
  </p>
  <p>Will set the unicode zodiac symbol of any date at the start of the command prompt. Try adding your birthday!</p>
</details>
