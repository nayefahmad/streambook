
import streamlit as __st
import streambook
__toc = streambook.TOCSidebar()
__toc._add(streambook.H1('Example 2'))
__toc._add(streambook.H1('Dataframes'))
__toc._add(streambook.H2('Subsection 1'))

__toc.generate()
__st.markdown(r"""<span id='Example 2'> </span>
# Example 2""", unsafe_allow_html=True)
__st.markdown(r"""This is a description of the project.

Some more stuff""", unsafe_allow_html=True)
with __st.echo(), streambook.st_stdout('info'):
    import numpy as np
    import pandas as pd
__st.markdown(r"""<span id='Dataframes'> </span>
# Dataframes""", unsafe_allow_html=True)
with __st.echo(), streambook.st_stdout('info'):
    df = pd.DataFrame({'a': np.linspace(0, 10, 50)})
with __st.echo(), streambook.st_stdout('info'):
    df.head()
__st.markdown(r"""<span id='Subsection 1'> </span>
## Subsection 1""", unsafe_allow_html=True)
__st.markdown(r"""This is a subsection.""", unsafe_allow_html=True)
__st.markdown(r"""End.""", unsafe_allow_html=True)

