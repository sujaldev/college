%! Class = ipu-c
%! Author = Sujal Singh
%! Date = 5/8/24

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipu-python}[A class for Python programming practical files for the Indraprastha University.]

\LoadClass[a4paper,12pt,twoside]{report}

% --- Packages ---
\RequirePackage{lmodern}
\RequirePackage{graphicx}
\RequirePackage{tabularray}
\RequirePackage{fancyhdr}
\RequirePackage[outputdir=./build]{minted}
\RequirePackage[most,minted,listings]{tcolorbox}
\RequirePackage[a4paper,hmargin=1.5cm,vmargin=2.25cm]{geometry}

% --- Arguments ---
\renewcommand{\@author}{Sujal Singh}
\newcommand{\@rollno}{04119051723} % what can one do, look up my GPA? I'll tell you, it's exactly mediocre (~50%ile).
\newcommand{\@batch}{IIOT--B1--23}
\renewcommand{\author}[1]{\renewcommand{\@author}{#1}}
\newcommand{\rollno}[1]{\renewcommand{\@rollno}{#1}}
\newcommand{\batch}[1]{\renewcommand{\@batch}{#1}}


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
        \textbf{\Huge Programming in Python (ICT 160)}\\[20pt]%
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
\pagestyle{fancy}
\fancyhead[LO]{\textbf{Programming in Python (ICT 160)}}
\fancyhead[RO]{\@author}
\fancyhead[LE]{\textbf{Practical File}}
\fancyhead[RE]{\@rollno}
\fancyfoot[RO]{Page \thepage~~}
\fancyfoot[LE]{~~Page \thepage}
\fancyfoot[C]{}
\renewcommand{\footrulewidth}{0.4pt}
\renewcommand{\headrulewidth}{0.4pt}


% --- Question Command ---
\newcounter{questions}
\setcounter{questions}{0}
\newcommand{\question}[1]{\stepcounter{questions}\noindent\textbf{\arabic{questions}. #1}\\\vspace*{10pt}}

% --- Figures ---
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
        stripall,
        breaklines,
        xleftmargin=10pt,
    },
    overlay={%
        \begin{tcbclipinterior}
            \draw [line width=1pt] (frame.north west) rectangle ([xshift=18pt]frame.south west);
        \end{tcbclipinterior}
    }}
\BeforeBeginEnvironment{code}{\vspace*{-18pt}}
