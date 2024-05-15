%! Class = CLASS_NAME
%! Author = sujal
%! Date = 5/11/24

\NeedsTeXFormat{LaTeX2e}
%! suppress = PackageNameDoesNotMatchFileName
\ProvidesPackage{ipu-ethics}[Quick class for submitting ethics assignment.]

\LoadClass[a4paper,twoside,11pt]{article}

% Packages
\RequirePackage{lmodern}
\RequirePackage[margin=2cm]{geometry}
\RequirePackage{setspace}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{enumitem}

% Title
\renewcommand{\maketitle}{%
    \pagestyle{plain}%
    \begin{center}%
        \LARGE\@title\\[\doublespace]%
        \large\@author\\[20pt]%
    \end{center}
    \\[10pt]\raggedright\normalsize%
}

% Headers and Footers
\fancypagestyle{plain}{
    \fancyhf{}
    \renewcommand{\headrulewidth}{0pt}
}
\fancypagestyle{fancy}{
    \fancyhf{}
    \fancyhead[LE]{Human Values \& Ethics}
    \fancyhead[RE]{Sujal Singh}
    \fancyhead[LO]{ICT144}
    \fancyhead[RO]{04119051723}
    \fancyhead[C]{\textbf{Assignment 1}}
    \fancyfoot[LE]{~~Page \thepage~of \pageref{LastPage}}
    \fancyfoot[RO]{Page \thepage~of \pageref{LastPage}~~}
    \renewcommand{\footrulewidth}{0.4pt}
    \renewcommand{\headrulewidth}{0.4pt}
}

% Questions
\newcounter{questions}
\setcounter{questions}{0}
