%! Class = ipu-math
%! Author = Sujal Singh
%! Date = 8/10/24

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipu-math}[A generic class for writing assignments in math courses.]

\LoadClass[a4paper,12pt,twoside]{report}

% --- Packages ---
\RequirePackage{lmodern}
\RequirePackage{fancyhdr}
\RequirePackage{enumitem}
\RequirePackage{tabularray}
\RequirePackage[a4paper,hmargin=0.75in,vmargin=0.5in,includeheadfoot,headsep=10pt]{geometry}
\RequirePackage{calc}


% --- Arguments ---
\renewcommand{\@author}{Sujal Singh}
\renewcommand{\author}[1]{\renewcommand{\@author}{#1}}

\newcommand{\@rollno}{04119051723}
\newcommand{\rollno}[1]{\renewcommand{\@rollno}{#1}}

\newcommand{\@batch}{IIOT--B1}
\newcommand{\batch}[1]{\renewcommand{\@batch}{#1}}

\newcommand{\@assignmentname}{Assignment}
\newcommand{\assignmentname}[1]{\renewcommand{\@assignmentname}{#1}}


% --- Header & Footer ---
\newcommand{\makestartheader}{%
    ~\vspace{-3em}%
    \begin{center}%
    \noindent\hrule\\[15pt]%
    \textbf{\large\@assignmentname}
    \\[5pt]%
    {\@author~--~\@rollno,~\@batch}%
    \\[15pt]\hrule\\[3em]%
    \end{center}}

\fancypagestyle{assignmentstart}{
    \fancyhf{}
    \renewcommand{\headrulewidth}{0pt}

    \fancyfoot[C]{Page \thepage}
    \renewcommand{\footrulewidth}{0.4pt}
}

\fancypagestyle{fancy}{
    \fancyhf{}
    \renewcommand{\headrulewidth}{0.4pt}
    \fancyhead[L]{\textbf{\small\@assignmentname}}
    \fancyhead[RE]{\small\@author}
    \fancyhead[RO]{\small\@batch~--~\@rollno}

    \fancyfoot[C]{Page \thepage}
    \renewcommand{\footrulewidth}{0.4pt}
}


% --- Counters ---
\newcounter{examples}

% --- Assignment commands ---
\newcommand{\startassignment}[1]{%
    \newpage%
%    \setcounter{page}{1}%
    \setcounter{examples}{1}%
    \assignmentname{#1}%
    \makestartheader\pagestyle{assignmentstart}}

% --- Content Commands --
\newcommand{\example}{\textbf{Example \arabic{examples}}\\[5pt]\stepcounter{examples}}
\newcommand{\solution}{\textbf{Solution:}\\[5pt]}
