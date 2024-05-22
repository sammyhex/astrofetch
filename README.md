<h1>Astrofetch</h1>
<h2 align=center>
  <img src="https://github.com/longtallsammy/astrofetch/assets/66911338/70f3813b-f371-4203-88c6-df621cf66431">
</h2>
<p><b>CLI fetch tool showing a logo for the current zodiac season, information about the season, and system specs. Includes a search tool to query dates or zodiac seasons. Unicode friendly!</b></p>
<h2>Usage:</h2>
<h3><b>Normal usage</b></h3>
<p></p>
<p>Show zodiac logo, season information, system specs.</p>
<b>
    
    astrofetch
  
</b>

<h3>Single-line mode</h3>
<p></p>
<p></p>Show time, date, season on a single line.</p>
<b>
    
    astrofetch -s
  
</b>
<p><b>Output:</b>
    
  >   14:36 May 18, Taurus season.
    
</p>

<details>
<summary>Unicode mode</summary>
  <p></p>
  <p>Show time, unicode symbol.</p>
  <b>

    astrofetch -s -u
    
  </b>
  <p><b>Output:</b>

  >  14:36  ♉
    
  </p>
</details>

<h3>Mini mode</h3>
<p></p>
<p>Show season name.</p>
<b>
    
    astrofetch -m
  
</b>
<p><b>Output:</b></p>
<p>
    
  >   Taurus
       
</p>
<details>
<summary>Unicode mode</summary>
  <p></p>
  <p>Show unicode symbol.</p>
  <b>

    astrofetch -m -u
    
  </b>
  <p><b>Output:</b>

  >   ♉
    
  </p>
</details>

<h3>Info mode</h3>
<p></p>
<p><b>Date search:</b></p>
<p>Query what season a date lies in.</p>
<b>
    
    astrofetch -i jan 1
  
</b>
<p><b>Output:</b>
    
   >  Capricorn season runs from December 22 to January 19.
    
</p>
<details>
<summary>Unicode mode</summary>
  <p><b>Date search:</b></p>
  <p></p>
  <p>Show unicode symbol of season.</p>
  <b>

    astrofetch -i jan 1 -u
    
  </b>
  <p><b>Output:</b>

   >  ♑
    
  </p>
</details>
<p><b>Sign search:</b></p>
<p>Search for information about a sign.</p>
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
<details>
 <summary>Unicode mode</summary>  
  <p></p>
  <p>Show unicode symbol of season, date information.</p>
  <b>

    astrofetch -i capricorn -u
    
  </b>
  <p><b>Output:</b></p>
  
   >  ♑ Dec 22 -> Jan 19
    
</details>
<h2>Notes:</h2>
<p>Only tested on Arch, Fedora, Pop, Ubuntu and Nix!</p>
