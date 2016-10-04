.. _todo:

*************************
Contributing to this Book
*************************

.. |--| unicode:: U+2013

This book is in the very early draft stages, so the structure and content may
change dramatically until the final release planned for late December 2015.
The following sections are some guidelines to stick to when making
contributions.

Book Structure
--------------

This book is split into three separate "books" concerning *Theory*, *Practice*,
and *Exploration*. The first covers base knowledge for the later sections, the
second covers practical knowledge, and the third touches upon extended topics
that students can explore later on.

The source files for the book are contained with the `source` folder. Each of
the books has their own subdirectory which contains their respective chapter
content.

Images related to a particular chapter should be kept in a folder called
`images` in the same directory as the chapter source file. For example, if you
were to add an image for a chapter within *Book 1: Theory*, you would place the
image in `source/book1_theory/images/new_image.png`.

Source Format
-------------

.. _Vim: http://www.vim.org/

ReStructuredText source files should be word-wrapped to 80 characters, which
can be easily done in `Vim`_ with the following key command: `vipgq`. This will
select the current paragraph the cursor is sitting on and will hard-wrap the
paragraph to 80 characters, assuming the property `textwidth` is set properly. 

Use soft-tabs (i.e. spaces) rather than using tab characters, including in
plot and code directives.

All source files are formatted in Unicode.

To keep the table of contents manageable, try to use the section header styles
below. Please make sure the header lines are the same width as the section
name:

* `#` with overline -- *Books*
* `*` with overline -- *Book chapters*
* `=` -- *Chapter sections*
* `-` -- *Chapter subsections*
* `^` -- *Chapter sub-sub-sections*

Color Scheme
------------

This is the color scheme used in the CCSM theme, please use these colors when
adding figures/plots or changing the theme:

.. raw:: html

   <table style="margin: 0 auto;"><tr>
      <td style="border: 1px solid #3E4349; padding: 24px; 
        background-color: #FFFFFF">#FFFFFF</td>
      <td style="padding: 24px; background-color: #F8B195">#F8B195</td>
      <td style="padding: 24px; background-color: #F07280">#F07280</td>
      <td style="padding: 24px; background-color: #C06C84">#C06C84</td>
      </tr><tr>
      <td style="padding: 24px; background-color: #6C5B7B; 
        color: #ffffff">#6C5B7B</td>
      <td style="padding: 24px; background-color: #39627d; 
        color: #ffffff">#39627D</td>
      <td style="padding: 24px; background-color: #3E4349;
        color: #ffffff">#3E4349</td>
   </tr></table>

Sections to Complete
====================

This is a tentative outline for how the book is going to be structured,
and it will be fleshed out more as development continues.

#. Principles of Waves -- **In Progress**
#. Sound Perception
#. Sampling Theory / DSP
#. Primitive Synthesis
#. Music Theory
#. Samplers + Granular Synthesis
#. Advanced Synthesis
#. Signal Processing
#. Algorithmic Composition
#. Future Explorations

   #. Live Coding
   #. Laptop Orchestras
   #. Embedded DSP (Arduinos, RasPis, etc.)

Todo List
=========

This is a compiled list of things that need to be added, changed, or
removed through the course of writing this book. If you have completed
one of these tasks, please send us a pull request!

.. todolist::

