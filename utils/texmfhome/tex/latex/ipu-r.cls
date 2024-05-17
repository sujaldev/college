%! Class = ipu-r
%! Author = Sujal Singh
%! Date = 5/15/24

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipu-r}[A class for R programming practical files for the Indraprastha University.]

\LoadClass[a4paper,12pt,twoside]{report}

% --- Packages ---
\RequirePackage{lmodern}
\RequirePackage{fancyhdr}
\RequirePackage{enumitem}
\RequirePackage{graphicx}
\RequirePackage{tabularray}
\RequirePackage[outputdir=./build]{minted}
\RequirePackage[most,minted,listings]{tcolorbox}
\RequirePackage[a4paper,hmargin=1.5cm,vmargin=1cm,includeheadfoot,headsep=10pt]{geometry}


% --- Arguments ---
\renewcommand{\@author}{Sujal Singh}
\newcommand{\@rollno}{04119051723}
\newcommand{\@batch}{IIOT--B1}
\newcommand{\@assignmentname}{Assignment}
\renewcommand{\author}[1]{\renewcommand{\@author}{#1}}
\newcommand{\rollno}[1]{\renewcommand{\@rollno}{#1}}
\newcommand{\batch}[1]{\renewcommand{\@batch}{#1}}
\newcommand{\assignmentname}[1]{\renewcommand{\@assignmentname}{#1}}

% --- Title Page ---
\renewcommand*{\maketitle}{
    \thispagestyle{empty}
    \pagenumbering{gobble}
    \vspace*{5pt}\noindent%
    \begin{minipage}{0.2\textwidth}
        \includegraphics[width=0.95\linewidth]{logo}~~~~~\vline
    \end{minipage}%
    \hfill%
    \begin{minipage}{0.75\textwidth}%
        \textbf{\Large Guru Gobind Singh Indraprastha University}\\[10pt]%
        {\large University School of Automation \& Robotics}
    \end{minipage}\vfill%
    \begin{center}
        \rule{\textwidth}{2pt}\\[30pt]%
        \textbf{\Large Probability and Statistics for Engineers Lab (BS110P)}\\[20pt]%
        \textbf{\LARGE Practical File}%
        \\[25pt]\rule{\textwidth}{2pt}\\\vfill%
        {\large\begin{tblr}{width=0.75\textwidth,colspec={|X[c]|X[c]|},rows=30pt,hlines}
                   \textbf{Name}              & \@author \\
                   \textbf{Enrollment Number} & \@rollno \\
                   \textbf{Batch}             & \@batch  \\
        \end{tblr}}\\[20pt]%
    \end{center}
    \newpage
    \pagenumbering{arabic}
}


% --- Header & Footer ---
\fancypagestyle{empty}{%
    \fancyhf{}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{assignmentstart}{
    \fancyhf{}
    \globaldefs=1
    \restoregeometry
    \newgeometry{hmargin=1.5cm,vmargin=1cm,includeheadfoot,headheight=60pt,headsep=20pt}
    \globaldefs=0
    \AddToHookNext{shipout/after}{%
        \globaldefs=1
        \restoregeometry
        \thispagestyle{fancy}
        \globaldefs=0
    }
    \fancyhead[C]{%
        \hrule\\[15pt]\textbf{\large\@assignmentname}\\[4pt]\@author~--~\@rollno,~\@batch\rule[-15pt]{0pt}{2ex}}
    \fancyfoot[C]{Page \thepage}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
}
\fancypagestyle{fancy}{
    \restoregeometry
    \fancyhf{}
    \fancyhead[L]{\@author}
    \fancyhead[C]{\textbf{\@assignmentname}}
    \fancyhead[RO]{\@batch}
    \fancyhead[RE]{\@rollno}
    \fancyfoot[C]{Page \thepage}
    \renewcommand{\footrulewidth}{0.4pt}
    \renewcommand{\headrulewidth}{0.4pt}
}

\pagestyle{fancy}


% --- Counters ---
\newcounter{questions}

% --- Assignment commands ---
\newcommand{\startassignment}[1]{%
    \newpage%
    \setcounter{page}{1}%
    \setcounter{questions}{0}%
    \assignmentname{#1}%
    \newpage\pagestyle{assignmentstart}}

% --- Question Commands ---
\newcommand{\@questionspacingvalue}{\\~\\}
\newcommand{\@questionspacing}{\@questionspacingvalue}

\newcommand{\question}[1]{\@questionspacing\stepcounter{questions}\noindent\textbf{\arabic{questions}. #1}\\}

\newcommand{\firstquestion}[1]{%
    \renewcommand{\@questionspacing}{}%
    \question{#1}%
    \renewcommand{\@questionspacing}{\@questionspacingvalue}}

\newcommand{\@figuretitle}{Output}
\newcommand{\outputfigure}[2][0.45]{%
    \noindent\textbf{\@figuretitle:}
    \begin{center}
        \includegraphics[width=#1\textwidth]{#2}
    \end{center}
}
\newcommand{\figurefigure}[2][0.45]{%
    \renewcommand{\@figuretitle}{Figure}%
    \outputfigure[#1]{#2}
    \renewcommand{\@figuretitle}{Output}%
}


% --- Code Environment ---
%\usemintedstyle{bw} % I figure why not have it colored for the digital version, I'll uncomment it when printing.
% Changes minted line number size
\renewcommand{\theFancyVerbLine}{\parbox{10pt}{\centering\footnotesize\arabic{FancyVerbLine}}}
\newtcblisting{code}[2]{
    listing only,
    listing engine=minted,
    minted language=#2,
    breakable,
    enhanced,
    colback=white,
    coltitle=black,
    colbacktitle=white,
    top=0pt,
    bottom=0pt,
    sharp corners,
    title=\textbf{#1:},
    minted options = {
        linenos,
%        stripall,
        breaklines,
        xleftmargin=10pt,
    },
    overlay={%
        \begin{tcbclipinterior}
            \draw [line width=1pt] (frame.north west) rectangle ([xshift=18pt]frame.south west);
        \end{tcbclipinterior}
    }}
\BeforeBeginEnvironment{code}{\vspace*{-18pt}}
