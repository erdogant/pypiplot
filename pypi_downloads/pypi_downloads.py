# --------------------------------------------------
# Name        : pypi_downloads.py
# Author      : E.Taskesen
# Contact     : erdogant@gmail.com
# github      : https://github.com/erdogant/pypi_downloads
# Licence     : See licences
# --------------------------------------------------

import os
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import pypistats
import requests
import matplotlib.pyplot as plt
import imagesc
curpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# %%

class pypi_downloads:

    def __init__(self, username, category=['with_mirrors', 'without_mirrors'], sep=';', verbose=3):
        self.username = username
        self.repo_link = 'https://api.github.com/users/' + username + '/repos'
        self.sep = sep
        self.category = category
        self.verbose=verbose

    def get_repo_names_from_git(self):
        # Extract repos for user
        if self.verbose>=3: print('[pypi_downloads] >Extracting repo names for [%s]..' %(self.username))
        r = requests.get(self.repo_link)
        data = r.json()

        # Extract the repo names
        repos = []
        for rep in data:
            # full_names.insert(0, rep['full_name'])
            repos.insert(0, rep['name'])
        if self.verbose>=3: print('[pypi_downloads] >[%.0d] repos found for [%s]' %(len(repos), self.username))
        # Return
        return np.array(repos)

    def update(self, repo=None):
        # Extract all repos
        repos = self.get_repo_names_from_git()
        # Check whether specific repo exists.
        if repo is not None:
            if not np.any(np.isin(repos, repo)): raise ValueError('[pypi_downloads] >Error: repos [%s] does not exists or is private.' %(repo))
            repos = [repo]

        if self.verbose>=3: print('[pypi_downloads] >Start updating..')
        for repo in repos:
            try:
                if self.verbose>=3: print('[pypi_downloads] >[%s]' %(repo))
                status = True
                df = pypistats.overall(repo, total=True, format="pandas")
                df.dropna(inplace=True)
                df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
                df = df.sort_values("date")
                df.reset_index(drop=True, inplace=True)
                del df['percent']

                # Merge with any on disk
                pathname = os.path.join(curpath, repo + '.csv')
                if os.path.isfile(pathname):
                    # Read repo from disk
                    df_disk = read_repo_counts_from_disk(pathname, self.sep)
                    # Merge with latest counts
                    df, status = add_new_counts_to_repo(df, df_disk, repo, verbose=self.verbose)
                # Write to disk
                if status:
                    df.to_csv(pathname, index=False, sep=self.sep)
            except:
                if self.verbose>=1: print('[pypi_downloads] >Skip [%s] coz not exists on Pypi.' %(repo))

    def get_repos(self):
        status = True
        # Retrieve all downloads from disk
        repos, filenames, pathnames = get_files_on_disk(verbose=self.verbose)
        # Update and retrieve if needed
        if len(repos)==0:
            if self.verbose>=3: print('[pypi_downloads] >No files found on disk. Lets update first!')
            # Update all repos
            self.update()
            # Retrieve all downloads from disk
            repos, filenames, pathnames = get_files_on_disk(verbose=0)
            if len(repos)==0:
                status = False
        # Return
        return status, repos, filenames, pathnames

    def stats(self, repo=None):
        status, repos, filenames, pathnames = self.get_repos()

        # Check whether specific repo exists.
        if repo is not None:
            Iloc = np.isin(repos, repo)
            if not np.any(Iloc): raise ValueError('[pypi_downloads] >Error: repos [%s] does not exists or is private. Tip: Run the .update() first.' %(repo))
            # repos = [repo]
            repos = repos[Iloc]
            filenames = filenames[Iloc]
            pathnames = pathnames[Iloc]

        if not status:
            if self.verbose>=3: print('[pypi_downloads] >No repos could be retrieved from git nor disk <return>')
            return None

        out = pd.DataFrame()
        for repo, pathname in zip(repos, pathnames):
            df = read_repo_counts_from_disk(pathname, self.sep)

            # Take desired categories
            Iloc = np.isin(df['category'], self.category)
            df = df.loc[Iloc, :]

            # Group by date
            df = df.groupby("date").sum().sort_values("date")
            df.reset_index(drop=False, inplace=True)

            dftmp = df.groupby("date").sum()
            dftmp.rename(columns = {'downloads': repo}, inplace=True)
            out = pd.concat([out, dftmp], axis=0)

        out.fillna(value=0, inplace=True)
        out.reset_index(drop=False, inplace=True)
        out = out.groupby("date").sum()
        
        heatmap = _compute_history_heatmap(out)

        self.results = {}
        self.results['data'] = out
        self.results['heatmap'] = heatmap
        return self.results

    def plot_more(self):
        # fig, ax = plt.subplots(figsize=(10, 2))
        # out.plot()

        # df['weeknr'] = df['date'].dt.week
        # df['cumsum'] = df['downloads'].cumsum()
        # ax.plot(df['weeknr'].values, df['cumsum'].values, label=repo)
        # ax.plot(df['weeknr'].values, df['downloads'].values, label=repo)

        # ax.legend()
        # ax.grid(True)

        # data = pypistats.overall("pillow", total=True, format="pandas")
        # df = df.groupby("category").get_group("without_mirrors").sort_values("date")
        # df = df.groupby("category").get_group("without_mirrors").sort_values("date")

        # chart = df.plot(x="date", y="downloads", figsize=(10, 2))
        # chart = df.plot(x="date", y="downloads", figsize=(10, 2))
        # chart.figure.show()
        # chart.figure.savefig("overall.png")  # alternatively
        pass

    def plot(self, title=None, description=None, path='d3heatmap.html', vmin=25, vmax=None):
        # if vmin is not None:
        #     vmin = df_heatmap.values.flatten()
        #     vmin = vmin[vmin>=10]
        #     vmin = np.min(vmin)
        if description is None:
            description = '%.0d Pypi downloads last year' %(self.results['heatmap'].sum().sum())
        if title is None:
            title = ''
        imagesc.d3(self.results['heatmap'], fontsize=9, title=title, description=description, path=path, width=700, height=200, cmap='interpolateGreens', vmin=vmin, vmax=vmax, stroke='black')


# %%
def _compute_history_heatmap(df, duration=364, nr_days=7):
    df = df.sum(axis=1).copy()
     # This is the number of columns in the plot
     # Number of rows
    datetimeformat='%Y-%m-%d'

    # Make sure the duration is tops 365 from now
    extend_days = datetime.now() - timedelta(duration)
    dates_start = pd.to_datetime(pd.date_range(start=extend_days, end=df.index[0]).strftime(datetimeformat), format=datetimeformat)
    df_start = pd.DataFrame(np.zeros((len(dates_start), 1)), dtype=int, index=dates_start)

    # Fill the gap between now and the latest point of the date in the data
    dates_end = pd.to_datetime(pd.date_range(start=df.index[-1] + timedelta(1), end=datetime.now()).strftime(datetimeformat), format=datetimeformat)
    df_end = pd.DataFrame(np.zeros((len(dates_end), 1)), dtype=int, index=dates_end)

    # dataframe containing 365 days of data
    df_365 = pd.concat([df_start, df, df_end], axis=0)

    # To make sure we can break the dataframe into columns of 7 days, we need to extend a bit more.
    extend_days = float(nr_days - np.mod(df_365.shape[0], nr_days))
    start = df_365.index[0] - timedelta(extend_days)
    dates_start = pd.to_datetime(pd.date_range(start=start, end=df_365.index[0] - timedelta(1)).strftime(datetimeformat), format=datetimeformat)
    df_start = pd.DataFrame(np.zeros((len(dates_start), 1)), dtype=int, index=dates_start)

    # Final
    df_fin = pd.concat([df_start, df_365], axis=0)
    df_values = df_fin.values.reshape((-1, nr_days))

    # Final heatmap with labels
    # month_name = df_fin.index.month_name().values
    # month_name = np.array(list(map(lambda x: x[0:3], month_name))).astype('O')
    # colnames = month_name + '_' + df_fin.index.week.astype(str).values

    colnames = df_fin.index.week.astype(str).values
    colnames = colnames.reshape((-1, nr_days))[:, -1]
    rownames = df_fin.index.day_name().values.reshape((-1, nr_days))[0, :]
    rownames = np.array(list(map(lambda x: x[0:3], rownames))).astype('O')
    # Flip matrix up down to make sure that sunday is on top
    rownames=rownames[::-1]
    df_values = np.flipud(df_values.T)

    # Output
    df_heatmap = pd.DataFrame(columns=colnames, data=df_values, index=rownames)

    return df_heatmap

# %%
def get_files_on_disk(verbose=3):
    if verbose>=3: print('[pypi_downloads] >Retrieve files from disk..')
    filenames = np.array(os.listdir(curpath))
    filesplit = np.array(list(map(os.path.splitext, filenames)))
    repos = filesplit[:, 0]
    Iloc = filesplit[:, 1]=='.csv'

    filenames = filenames[Iloc]
    repos = repos[Iloc]
    # Make full path
    pathnames = np.array(list(map(lambda x: os.path.join(curpath, x), filenames)))
    return repos, filenames, pathnames 

def read_repo_counts_from_disk(pathname, sep):
    df_disk = pd.read_csv(pathname, sep=sep)
    df_disk['date'] = pd.to_datetime(df_disk['date'], format='%Y-%m-%d')
    return df_disk

def add_new_counts_to_repo(df, df_disk, repo, verbose=3):
    STATUS = False
    count_before = df.shape[0]
    df = pd.concat([df, df_disk], axis=0)
    df.drop_duplicates(inplace=True)
    df = df.sort_values("date")
    df.reset_index(drop=True, inplace=True)

    count_after = df.shape[0]
    if count_after>count_before:
        STATUS=True
        if verbose>=3: print('[pypi_downloads] >[%s] updated.' %(repo))

    return df, STATUS

# %% Main
# if __name__ == "__main__":
#     import pypi_downloads as pypi_downloads
#     df = pypi_downloads.import_example()
#     out = pypi_downloads.fit(df)
#     fig,ax = pypi_downloads.plot(out)
